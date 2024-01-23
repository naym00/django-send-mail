from django.urls import path
from myapp import views

urlpatterns = [
    path('get-students/', views.getStudents, name='get-students'),
    path('filter-students/', views.filterStudents, name='filter-students'),
    path('add-student/', views.addStudent, name='add-student'),
    path('email_sending/', views.email_sending, name='email sending'),
    path('email-sending-including-files/', views.email_sending_including_files, name='email-sending-including-files'),
]
