import os

from django.db.models import Prefetch
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

import requests

from cv2 import settings
from .email import send_letter
from .forms import ContactsForm
from .models import (
    Profile,
    SkillCategory,
    Skill,
    Experience,
    Project,
    ProjectImage
)
from .utils import get_svelte_manifest


def ResultEncoder(obj):
    if isinstance(obj, Profile):
        return {
            'id': obj.id,
            'name': obj.name,
            'lastname': obj.lastname,
            'image': obj.image.url if obj.image else None,
            'occupation': obj.occupation,
            'description': obj.description,
            'phone': obj.phone,
            'email': obj.email,
            'whatsapp': obj.whatsapp,
            'telegram': obj.telegram,
            'linkedin': obj.linkedin,
            'github': obj.github,
            'cv': obj.cv
        }

    if isinstance(obj, SkillCategory):
        return {
            'id': obj.id,
            'name': obj.name,
            'skills': [ResultEncoder(item) for item in obj.skills.all()]
        }

    if isinstance(obj, Skill):
        return {
            'id': obj.id,
            'category': {
                'name': obj.category.name
            },
            'name': obj.name,
            'level': obj.level,
            'image': obj.image.url if obj.image else None,
            'skill_url': obj.skill_url
        }

    if isinstance(obj, Experience):
        return {
            'id': obj.id,
            'skills': [ResultEncoder(item) for item in obj.skills.all()],
            'company': obj.company,
            'company_url': obj.company_url,
            'position': obj.position,
            'start_date': obj.start_date.strftime('%Y-%m-%d'),
            'end_date': obj.end_date.strftime('%Y-%m-%d') if obj.end_date else None,
            'is_current': obj.is_current,
            'achievements': obj.achievements
        }

    if isinstance(obj, Project):
        return {
            'id': obj.id,
            'title': obj.title,
            'description': obj.description,
            'images': [
                img.image.url for img in obj.images.all() if img.image
            ],
            'technologies': [{
                'category': {
                    'name': value.category.name
                },
                'name': value.name,
                'level': value.level,
                'image': value.image.url if value.image else None
            } for value in obj.technologies.all()],
            'github_url': obj.github_url,
            'live_demo_url': obj.live_demo_url
        }


def index(request):
    if request.headers.get('Accept') == 'application/json':
        try:
            if request.method == 'POST':
                form = ContactsForm(request.POST)

                if form.is_valid():
                    name = form.cleaned_data['name']
                    email = form.cleaned_data['email']
                    subject = form.cleaned_data['subject']
                    message = form.cleaned_data['message']

                    recaptcha_token = request.POST.get('recaptcha_token')

                    data = {
                        'secret': settings.RECAPTCHA_PRIVATE_KEY,
                        'response': recaptcha_token
                    }

                    r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)

                    result = r.json()

                    if result.get('success') and result.get('score', 0) >= 0.5:
                        send_letter(name, email, message)

                        return JsonResponse({
                            'status': 'success',
                            'message': _('Ваше сообщение успешно отправлено')
                        })

                    else:
                        return JsonResponse({
                            'status': 'error',
                            'message': _('Проверка безопасности не пройдена. Попробуйте еще раз.'),
                            'errors':  [{'message': _('Низкий рейтинг reCAPTCHA. Попробуйте обновить страницу.')}]
                        })

                else:
                    return JsonResponse({
                        'status': 'error',
                        'errors': form.errors.get_json_data()
                    })

            form = ContactsForm()

            return JsonResponse({
                'status': 'success',
                'profile': ResultEncoder(Profile.get_profile_data()),
                'categories': [ResultEncoder(item) for item in SkillCategory.objects.filter(is_published=True).prefetch_related('skills__image')],
                'skills': [ResultEncoder(skill) for skill in Skill.objects.filter(is_published=True)],
                'certificates': [ResultEncoder(skill) for skill in Skill.objects.filter(is_published=True, category__name='Certificate')],
                'frontendSkills': [ResultEncoder(skill) for skill in Skill.objects.filter(is_published=True, category__name='Frontend')],
                'backendSkills': [ResultEncoder(skill) for skill in Skill.objects.filter(is_published=True, category__name='Backend')],
                'experience': [ResultEncoder(item) for item in Experience.objects.filter(is_published=True)],
                'projects': [ResultEncoder(item) for item in Project.objects.filter(is_published=True).prefetch_related(
                    Prefetch(
                        'technologies',
                        queryset=Skill.objects.select_related('category')
                    ),
                    Prefetch(
                        'images',
                        queryset=ProjectImage.objects.filter(is_published=True),
                    )
                ).order_by('order_by')],
                'form': {
                    field.name: {
                        'label': str(field.label),
                        'required': field.field.required,
                        'input_type': getattr(field.field.widget, 'input_type', 'textarea'),
                        'initial': field.value() if field.value else '',
                        'help_text': str(field.field.help_text),
                        'choices': getattr(field.field, 'choices', None)
                    } for field in form
                }
            })

        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            })

    manifest = get_svelte_manifest(
        os.path.join(
            settings.BASE_DIR,
            'main',
            'static',
            'svelte',
            'assets',
            '.vite'
        )
    ).get('index.html', {})

    ctx = {
        'site_key': settings.RECAPTCHA_PUBLIC_KEY,
        'manifest_css': manifest.get('css', []),
        'manifest_js': manifest.get('file', '')
    }

    return render(request, 'main/index.html', ctx)
