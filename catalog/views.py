from django.shortcuts import redirect, render
from .models import Goods
from .forms import GoodsForm
from django.views.generic import DetailView, UpdateView, DeleteView

def catalog_home(request):
    goods = Goods.objects.order_by('title')
    return render(request, 'catalog/catalog_home.html', {'goods': goods})


class CatalogDetailView(DetailView):
    model = Goods
    template_name = 'catalog/details_view.html'
    context_object_name = 'good'


class CatalogUpdateView(UpdateView):
    model = Goods
    template_name = 'catalog/create.html'
    
    form_class = GoodsForm


class CatalogDeleteView(DeleteView):
    model = Goods
    context_object_name = 'good'
    template_name = 'catalog/catalog_delete.html'
    success_url = '/catalog'
    
    


def create(request):
    error = ''
    if request.method == 'POST':
        form = GoodsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalog_home')
        else:
            error = "Форма заполнена некорректно"

    form = GoodsForm
    data = {
        'form': form,
        'error': error
    }

    return render(request, 'catalog/create.html', data)
