from django.shortcuts import render


def item_list(request):
    template_name = 'catalog/catalog.html'
    content = {}
    return render(request, template_name, content)


def item_detail(request, pk):
    template_name = 'catalog/catalog_item.html'
    content = {'pk': pk}
    return render(request, template_name, content)
