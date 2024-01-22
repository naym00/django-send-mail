from django.urls import path
from myapp.views import email_sending

urlpatterns = [
    path('', email_sending, name='email sending'),
]
