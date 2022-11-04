from django.urls import path
from .import views

urlpatterns = [
    path('',views.api_show, name='api_show'),
    path('tasklist/',views.list_task, name='tasklist'),
    path('taskcreate/',views.create_task, name='taskcreate'),
    path('taskdetail/<str:pk>', views.details_task, name='taskdetail'),
]