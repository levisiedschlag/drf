from unicodedata import name
from django.urls import path
from api import views

app_name='app_api'

urlpatterns = [
    path('', views.api_home, name="api_home")
]