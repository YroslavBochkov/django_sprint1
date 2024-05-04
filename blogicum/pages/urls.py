# pages/urls.py
from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('rules/', views.rules, name='rules'),
    path('category/<slug:category_slug>/', views.category, name='category'),
    path('index/', views.index, name='index'),
    path('detail/', views.detail, name='detail'),
]
