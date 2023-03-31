from django.urls import path
from .views import HomeView, get_category

urlpatterns = [
    path('', HomeView, name = 'home'),
    path('cat/<int:category_id>/', get_category, name = 'category'),
]