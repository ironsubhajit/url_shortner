from django.urls import path
from . import views as shortener_views


urlpatterns = [
    path('', shortener_views.base, name="home"),
    path('about', shortener_views.about, name="about"),
    path('create', shortener_views.create, name="create"),
    path('go/<str:pk>', shortener_views.go, name="go"),
]
