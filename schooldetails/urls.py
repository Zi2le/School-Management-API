from django.urls import path, include
from .import views 
#from rest_framework.authtoken import views as drf_view
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns=[
    path('course/', views.CourseListView.as_view(), name="course"),
    path('course/<int:pk>/', views.CourseDetail.as_view(), name="course"),
    # path("token_login/", obtain_auth_token, name="token_login"),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('students/', views.StudentApiView.as_view(), name="students"),
    path('teacher/', views.TeacherListView.as_view(), name="teacher"),
    path('students/<int:pk>/', views.StudentDetailView.as_view(), name="students"),
    # path('user/', views.CreateNewUser.as_view(), name="new_user"),


]