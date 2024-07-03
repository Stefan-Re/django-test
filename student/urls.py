from django.urls import path

from student import views

urlpatterns = [
    path('create_student/', views.StudentCreateView.as_view(), name='create-student'),
    path('students_list/', views.StudentListView.as_view(), name='students-list'),
    path('update_student/<int:pk>/', views.StudentUpdateView.as_view(), name='update-student'),
    path('delete_student/<int:pk>/', views.StudentDeleteView.as_view(), name='delete-student'),
    path('students_detail/<int:pk>/', views.StudentDetailView.as_view(), name='students-detail'),
    path('student_history/', views.HistoryStudentListView.as_view(), name='student-history'),
]
