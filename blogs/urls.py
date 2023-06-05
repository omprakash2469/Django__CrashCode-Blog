
from django.urls import path

from . import views

urlpatterns = [
    path('search/', views.search, name="search"),
    path('<slug:category_slug>/<slug:slug>', views.blogDetails, name="post-details"),
    path('<slug:slug>', views.categoryDetails, name="category-details"),
]