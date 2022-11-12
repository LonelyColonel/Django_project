from django.http import HttpResponse
from django.shortcuts import render


def description(request):
    template_name = 'about/about.html'
    content = {}
    return render(request, template_name, content)
