from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='BlogHome'),
    path('about/', views.about, name='About'),
    path('contact/', views.contact, name='Contact'),
    path('FAQs/', views.FAQs, name='FAQs'),
    path('post/', views.post, name='post'),
    path('search/', views.search, name='Search'),
    path('blogview/<int:myid>', views.blogView, name='blogview'),
]
