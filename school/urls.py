from django.urls import path
from . import views 

urlpatterns = [
    path('', views.HomeListView.as_view(), name='index'),
    path('courses', views.CoursesListView.as_view(), name='courses'),
    path('course_details/<int:pk>/', views.CourseDetailView.as_view(), name='course_details'),
    path('course_details/<int:pk>/reserve/', views.handle_reservation, name='handle_reservation'),
    path('trainers', views.trainers, name='trainers'),
    path('about', views.about, name='about'),
]