from django.urls import path
from . import views

urlpatterns = [

    path('courses/', views.course_list_create),
    path('courses/<int:pk>/', views.course_detail),
 
]
