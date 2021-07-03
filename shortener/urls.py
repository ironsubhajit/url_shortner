from django.urls import path
from . import views as shortener_views


urlpatterns = [
    path('', shortener_views.base, name="home"),
    path('about', shortener_views.about, name="about"),
    path('create', shortener_views.create, name="create"),
    path(
        'createurl',
         shortener_views.create_user_url,
         name="create_user_url"
         ),
    path('go/<str:pk>', shortener_views.go, name="go"),
    path('g/<str:pk>', shortener_views.user_url_go, name="user_url_go"),
]
