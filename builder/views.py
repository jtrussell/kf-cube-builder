from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'builder/form_page.html', context)


def results(request):
    context = {}
    return render(request, 'builder/results_page.html', context)