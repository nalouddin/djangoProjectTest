from django.urls import path
from .views import HomeView, get_category

urlpatterns = [
    path('', HomeView, name = 'home'),
    path('category/<int:category_id>/', get_category),
]