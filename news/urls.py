from django.urls import path
from .views import HomeView, get_category

urlpatterns = [
    path('category/<int:category_id>/', get_category, name = 'category'),
    path('', HomeView, name = 'home'),
]