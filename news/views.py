from django.shortcuts import render
from .models import News

# Create your views here.

def HomeView(request):
    news = News.objects.all()
    context = {
        'news': news,
    }
    title = 'Yangliklar saiti'
    return render(request, 'news/home.html', context)