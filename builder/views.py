from django.shortcuts import render


def index(request):
    return render(request, 'builder/form_page.html', {})


def results(request):
    return render(request, 'builder/results_page.html', {})


def error(request):
    return render(request, 'builder/error_page.html', {
        'errorMessage': 'That username does\'t exist!'
    })

