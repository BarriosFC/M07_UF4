from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teachers', views.teachers, name='teachers'),
    path('students', views.students, name='students'),
    path('user/<str:id>/', views.user, name='usuario'),
    path('user-form/', views.user_form, name='user_form')
]