from django.http import JsonResponse
from django.utils.translation import gettext_lazy as _

from .models import (
    Profile,
    SkillCategory,
    Skill,
    Experience,
    Project
)


def index(request):
    try:
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
                    'skills': [ResultEncoder(item) for item in obj.skills.all()],
                }

            if isinstance(obj, Skill):
                return {
                    'id': obj.id,
                    'category': {
                        'name': obj.category.name
                    },
                    'name': obj.name,
                    'level': obj.level,
                    'image': obj.image.url if obj.image else None
                }

            if isinstance(obj, Experience):
                return {
                    'id': obj.id,
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
                    'slug': obj.slug,
                    'description': obj.description,
                    'image': obj.image,
                    'technologies': [{
                        'category': {
                            'name': value.category.name
                        },
                        'name': value.name,
                        'level': value.level,
                        'image': value.image
                    } for value in obj.technologies.all()],
                    'github_url': obj.github_url,
                    'live_demo_url': obj.live_demo_url,
                }

        return JsonResponse({
            'status': 'success',
            # 'title': _('Давид Хурцидзе'),
            'profile': ResultEncoder(Profile.get_profile_data()),
            'categories': [ResultEncoder(item) for item in SkillCategory.objects.prefetch_related('skills__image').all()],
            # 'skills': Skill.objects.select_related('category', 'image').all(),
            'experience': [ResultEncoder(item) for item in Experience.objects.filter(is_published=True)],
            'projects': [ResultEncoder(item) for item in Project.objects.prefetch_related(
                'technologies',
                'technologies__category',
                'technologies__image',
            ).select_related('image').filter(is_published=True)]
        })

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': _(f'{e}')
        })
