from django.urls import path
from certificates.views import home


urlpatterns = [
    path('', home)
]