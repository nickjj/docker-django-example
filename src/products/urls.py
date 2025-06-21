from django.contrib import admin
from django.urls import path 
from products.views import ProductListView, ProductDetailView, ProtectedListView
urlpatterns = [
    path("admin/", admin.site.urls),
    path("products/", ProductListView.as_view()),
    path("products/<int:pk>", ProductDetailView.as_view()),
    path("my-products/", ProtectedListView.as_view()),
]