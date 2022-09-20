from django.urls import path
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
from . import views
from .forms import PwdResetConfirmForm, PwdResetForm, UserLoginForm

app_name = 'account'

urlpatterns = [
    path('register/', views.account_register, name='register'),
    path('activate/<slug:uidb64>/<slug:token>/',
         views.account_activate, name='activate'),
    path('login/', auth_views.LoginView.as_view(template_name='account/registration/login.html',
                                                form_class=UserLoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/account/login/'), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('profile/edit/', views.edit_details, name='edit-details'),
    path('profile/delete_user/', views.delete_user, name='delete-user'),
    path('profile/delete_confirm/', TemplateView.as_view(
        template_name="account/user/delete_confirm.html"), name='delete-confirmation'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="account/user/password_reset_form.html",
                                                                 success_url='password_reset_email_confirm',
                                                                 email_template_name='account/user/password_reset_email.html',
                                                                 form_class=PwdResetForm), name='pwdreset'),
    path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='account/user/password_reset_confirm.html',
                                                                                                success_url='/account/password_reset_complete/',
                                                                                                form_class=PwdResetConfirmForm),
         name="password-reset-confirm"),
    path('password_reset/password_reset_email_confirm/',
         TemplateView.as_view(template_name="account/user/reset_status.html"), name='password-reset-done'),
    path('password_reset_complete/',
         TemplateView.as_view(template_name="account/user/reset_status.html"), name='password-reset-complete'),
]
