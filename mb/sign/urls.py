from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import usual_login_view, login_with_code_view

app_name = 'sign'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='../templates/sign/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='../templates/sign/logout.html'), name='logout'),
    path('signup/', usual_login_view, name='signup'),
    path('signup-code/', login_with_code_view, name='signup_code'),

]