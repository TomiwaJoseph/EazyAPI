from django.urls import path
from .views import index, documentation, generate_url, ProductView

urlpatterns = [
    path('', index, name='index'),
    path('docs/', documentation, name='docs'),
    path('generate-url/', generate_url, name='generate_url'),
    path('query/', ProductView.as_view(), name='api_query')
]
