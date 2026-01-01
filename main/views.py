from django.shortcuts import render

def index(request):
    context = {
        'Title': 'About'
    }

    return render(request, 'about.html', context=context)
