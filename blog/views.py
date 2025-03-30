import requests
from rest_framework import generics
from rest_framework.response import Response
from .models import Blog
from .serializers import BlogSerializer

class BlogListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogDetailView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class CountryInfoView(generics.GenericAPIView):
    def get(self, request, country_name):
        url = f"https://restcountries.com/v3.1/name/{country_name}"
        response = requests.get(url)
        if response.status_code == 200:
            return Response(response.json())
        return Response({"error": "Country not found"}, status=404)

