from django.urls import path
from .views import TaskAPICreate, TaskAPIGet, CreateItemView, TaskAPIList,TaskDeleteView,UpdateTask

urlpatterns=[
    path(r"get/<int:pk>", TaskAPIGet.as_view(), name='TaskGet'),
    path(r'create', TaskAPICreate.as_view(), name='TaskCreate'),
    path('list', TaskAPIList.as_view() , name= 'TaskList'),
    path(r'update/<int:pk>/', UpdateTask.as_view(), name='TaskUpdate'),
    path(r'deletetask/<int:pk>/', TaskDeleteView.as_view(), name='TaskDelete'),
    path(r'create-task', CreateItemView.as_view(), name='task')

]
