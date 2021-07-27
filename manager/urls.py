# Django Libs:
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from django.conf import settings

# Local Libs:
from . import views


urlpatterns = [
    path("", RedirectView.as_view(url="admin/")),
    path(
        "reset_password/",
        auth_views.PasswordResetView.as_view(
            html_email_template_name="../templates/registration/password_reset_email.html",
            extra_email_context={'MEDIA_URL': settings.MEDIA_URL}
        ),
        name="admin_password_reset",
    ),
    path(
        "reset_password_sent/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset_password/<uidb64>/<token>",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset_password_complete/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
