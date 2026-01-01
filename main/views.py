from django.shortcuts import render

from django.utils.translation import gettext_lazy as _

from main.models import Profile


def index(request):
    context = {
        'title': _('Обо мне'),
        'profile': Profile.get_profile_data()
    }

    return render(request, 'about.html', context=context)
