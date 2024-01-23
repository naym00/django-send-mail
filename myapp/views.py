from helps.common.generic import Commonhelps as ghelp
from myapp.serializer import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponse
from rest_framework import status
from myapp.models import Student


@api_view(['GET'])
def getStudents(request):
    students = Student.objects.all()
    studentserializer = StudentSerializer(students, many=True)
    return Response(studentserializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def filterStudents(request):
    extra_conditions = {'name': 'icontains', 'gender': 'iexact'}
    students = ghelp().filterClass(Student, request, extra_conditions)
    student_count = students.count()
    studentserializer = StudentSerializer(students, many=True)
    return Response({'count': student_count, 'data': studentserializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
def addStudent(request):
    studentserializer = StudentSerializer(data=request.data, many=False)
    if studentserializer.is_valid():
        studentserializer.save()
        return Response(studentserializer.data, status=status.HTTP_201_CREATED)




@api_view(['GET'])
def email_sending(request):
    # email_from = settings.EMAIL_HOST_USER
    email_from = None
    recipient_list = ['xxxx@gmail.com']
    send_mail('A B C', 'dummy message', email_from, recipient_list)
    return HttpResponse(f"Check {recipient_list[0] if len(recipient_list) == 1 else ', '.join(recipient_list)}")

@api_view(['GET'])
def email_sending_including_files(request):
    
    # email_from = settings.EMAIL_HOST_USER
    email_from = None
    recipient_list = ['xxxx@gmail.com']
    attachments = ['myapp/static/images/446c9c5d6dafebba3f765a7a6dd07c9f.jpg', 'myapp/static/pdf/Md_Nymur_Rahman_Progress_Report_December-January.pdf']
    email = EmailMessage('A B C', 'dummy message', email_from, recipient_list)
    for attachment in attachments:
        email.attach_file(attachment)
    email.send()
    return HttpResponse(f"Check {recipient_list[0] if len(recipient_list) == 1 else ', '.join(recipient_list)}")