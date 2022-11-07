from django.urls import path, include
from .views import emailcheck
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', emailcheck, name='email_check'),

]