from django.urls import path

from . import views

app_name = 'certificates'

urlpatterns = [
    path('', views.home, name="home"),
    path('certificates  /search/', views.search, name="search"),
    path('certificates/<int:id>/', views.certificate, name="certificate"),

    path('certificates/category/<int:category_id>/',
         views.category, name="category"),
]
