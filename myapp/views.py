
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings

def email_sending(request):
    # email_from = settings.EMAIL_HOST_USER
    email_from = None
    recipient_list = ['naymhsain00@gmail.com', 'sathy754@gmail.com']
    send_mail('A B C', 'dummy message', email_from, recipient_list)
    return HttpResponse(f"Check {recipient_list[0] if len(recipient_list) == 1 else ', '.join(recipient_list)}")