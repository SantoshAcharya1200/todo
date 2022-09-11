from . import views
from django.urls import path
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.TaskList.as_view(), name='home'),
    path('login/', views.CreateLoginView.as_view(), name='login'),
    path('register/', views.RegisterPage.as_view(), name='register'),
    path('wordle/', views.WordleView.as_view(), name='wordle'),
    path('logout/', LogoutView.as_view(next_page = 'login'), name='logout'),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name='task'),
    path('create-task/', views.TaskCreate.as_view(), name='create-task'),
    path('update-task/<int:pk>/', views.TaskUpdate.as_view(), name='update-task'),
    path('update-delete/<int:pk>/', views.TaskDelete.as_view(), name='update-delete'),

]