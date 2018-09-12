from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product

class SearchProductView(ListView):

    template_name = 'search/view.html'

    def get_context_data(self, **kwargs):
        context = super(SearchProductView, self).get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self, **kwargs):
        request = self.request
        print(request.GET)
        query = request.GET.get('q')
        if query is not None:
            return Product.objects.search(query)
        return Product.objects.none()

