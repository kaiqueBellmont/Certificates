from django.urls import path
from . import views

app_name = 'certificates'

urlpatterns = [
    path('', views.home, name="home"),
    path('certificates/<int:id>/', views.certificate, name="certificate"),
]
