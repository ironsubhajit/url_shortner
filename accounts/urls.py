from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from . import (
    views as acc_views,
    forms as acc_form
)

app_name = 'accounts'

urlpatterns = [
    path('signup/', acc_views.SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(
            template_name='accounts/login.html',
            authentication_form=acc_form.UserLoginForm
            ),
         name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
