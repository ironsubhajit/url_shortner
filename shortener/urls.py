from django.urls import path
from . import views as shortener_views


urlpatterns = [
    path('', shortener_views.base, name="home"),
]
