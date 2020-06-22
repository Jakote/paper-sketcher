from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('login', views.login, name='login'),
     path('signup', views.signup, name='signup'),
     path('home', views.home, name='home'),
     path('sketch', views.sketch, name='sketch'),
     path('profile', views.profile, name='profile'),
     path('pdf_templates', views.pdf_templates, name='pdf_templates'),
     path('generate_paper', views.generate_paper, name='generate_paper'),
]