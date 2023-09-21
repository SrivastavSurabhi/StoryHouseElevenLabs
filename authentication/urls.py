from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('login', login, name="login"),
    path('logout', logout_view, name="logout"),
    path('profile', profile_view, name="profile"),
    path('forgot_password', forgot_password, name="forgot_password"),
    path('password-reset/<uid>', password_reset, name="password_reset"),
    path('media/<path:path>', media_files, name="secure"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)