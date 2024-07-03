from django.urls import path

from trainer import views

urlpatterns = \
    [path('create_trainer/', views.TrainerCreateView.as_view(), name='create-trainer'),
     path('trainer_list/', views.TrainerListView.as_view(), name='trainer-list'),
     path('update_trainer/<int:pk>/', views.TrainerUpdateView.as_view(), name='update-trainer'),
     path('delete_trainer/<int:pk>/', views.TrainerDeleteView.as_view(), name='delete-trainer'),
     path('trainer_detail/<int:pk>/', views.TrainerDetailView.as_view(), name='trainer-detail'),
     path('get_all_students_per_trainers/<int:pk>', views.get_all_students_per_trainer, name='get-all-students'),
]
