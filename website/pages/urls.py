from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('installation/', views.installation, name='installation'),
    path('tutorial/', views.tutorial, name='tutorial'),
    path('results/', views.results, name='results'),
    path('conclusion/', views.conclusion, name='conclusion'),
    path('credits/', views.references, name='credits'),
]