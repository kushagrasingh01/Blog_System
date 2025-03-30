from django.urls import path
from .views import BlogListCreateView, BlogDetailView, CountryInfoView

urlpatterns = [
    path('blogs/', BlogListCreateView.as_view(), name='blog-list'),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('country/<str:country_name>/', CountryInfoView.as_view(), name='country-info'),
]
