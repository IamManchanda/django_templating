from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexPageView.as_view(), name = 'index'),
    path('about-us/', views.AboutUsPageView.as_view(), name = 'about-us'),
    path('contact-us/', views.ContactUsPageView.as_view(), name = 'contact-us'),
]