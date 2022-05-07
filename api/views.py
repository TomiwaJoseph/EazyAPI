from rest_framework import generics
from django.shortcuts import render
from .forms import APIForm
from .models import Product
from .serializers import ProductSerializer
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.sites.shortcuts import get_current_site


class ProductView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = ProductSerializer
        
    def get(self, request, *args, **kwargs):
        category = self.request.GET.get('category')
        title = self.request.GET.get('title')
        limit = self.request.GET.get('limit')
        invalid_parameter = False
        
        try:
            correct_category = category.title() in ['All', 'Desktops', 'Laptops', 'Hybrids', 'Tablets']
            if not correct_category:
                raise Exception
            
            limit = int(limit)
            if limit < 1 or limit > 15:
                raise Exception
            
            if category.lower() == 'all':
                products = list(Product.objects.filter(
                    Q(title__contains=title)
                ).distinct())[:limit]
            else:
                products = list(Product.objects.filter(
                    Q(category__title__contains=category)&
                    Q(title__contains=title)
                ).distinct())[:limit]
        except:
            products = []
            invalid_parameter = True
        
        serializer = ProductSerializer(products, many=True)
        new_serializer = list(serializer.data)
        length_of_db_products = len(products)
        
        if length_of_db_products:
            new_serializer.append({'response_code': 0})
        elif invalid_parameter:
            new_serializer.append({'response_code': 2})
        elif length_of_db_products == 0:
            new_serializer.append({'response_code': 1})
                    
        return JsonResponse(new_serializer, safe=False)


def index(request):
    return render(request, 'api/index.html')

def documentation(request):
    return render(request, 'api/docs.html')

def generate_url(request):
    if request.method == 'POST':
        form = APIForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data.get('category')
            title = form.cleaned_data.get('title')
            limit = form.cleaned_data.get('limit')
            api_url = str(get_current_site(request)) + f'/api/query/?category={category}&title={title}&limit={limit}'
            context = {
                'form': form,
                'api_url': api_url,
            }
            return render(request, 'api/generate_url.html', context)
    form = APIForm()
    return render(request, 'api/generate_url.html', {'form': form})

