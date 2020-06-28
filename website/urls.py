from django.urls import path
from website import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('about/', views.aboutus, name='aboutus'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('gallery/', views.gallery, name='gallery'),
    path('pricing/', views.pricing, name='pricing'),
]