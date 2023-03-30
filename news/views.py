from django.shortcuts import render
from .models import News

# Create your views here.

def HomeView(request):
    news = News.objects.all()
    context = {
        'news': news,
    }
    return render(request, 'home.html', context)