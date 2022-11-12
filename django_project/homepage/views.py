from django.shortcuts import render


def home(request):
    template_name = 'homepage/index.html'
    content = {}
    return render(request, template_name, content)
