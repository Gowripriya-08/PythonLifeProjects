from django.urls import path
from .import views

urlpatterns = [
    path('add_students/',views.add_student),
    path('add_marks/',views.add_marks),
    path('view_students/',views.view_students),
    path('edit_student/', views.edit_student,name='edit_Students'),
]