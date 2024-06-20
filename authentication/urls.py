from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("login", views.login_view, name='login'),
    path("register", views.register_view),
    path("logout", views.logout_view),

    #reset passwords URLs:
    path('reset_password/', views.CustomPasswordResetView.as_view(template_name="authentication/pages/registration/password_reset_form.html"), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="authentication/pages/registration/password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="authentication/pages/registration/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="authentication/pages/registration/password_reset_complete.html"), name='password_reset_complete'),
    
]