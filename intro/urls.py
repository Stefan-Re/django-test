from django.urls import path

from intro import views

urlpatterns = [
    path('first_page/', views.index, name='first-page'),
    path('second_page/', views.show_name, name='second-page'),
    path('cars/', views.cars, name='list-cars'),
    path('phones/', views.phones, name='list-phones'),
    path('data/', views.get_data, name='data')
]
