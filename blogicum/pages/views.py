# pages/views.py
from django.shortcuts import render

def about(request):
    return render(request, 'pages/about.html')

def rules(request):
    return render(request, 'pages/rules.html')

def category(request, category_slug):  # Исправлено: Имя функции должно быть 'category', а не 'categoryrequest'
    return render(request, 'blog/category.html', {'category_slug': category_slug})  # Исправлено: Указан правильный путь к шаблону 'category.html'

def index(request):
    return render(request, 'index.html')