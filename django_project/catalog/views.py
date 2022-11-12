from django.http import HttpResponse
from django.shortcuts import render


def item_list(request):
    template_name = 'catalog/catalog.html'
    content = {}
    return render(request, template_name, content)


def item_detail(request, pk):
    return HttpResponse(f'Подробно элемент {pk}')
