from django.http import JsonResponse
from django.shortcuts import render

from django.utils.translation import gettext_lazy as _

from main.models import Profile


def index(request):
    ctx = {
        'status': 'success',
        'title': _('Обо мне'),
        'profile': Profile.get_profile_data()
    }

    # return JsonResponse(ctx)

    return render(request, 'about.html', context=ctx)
