from django.urls import path
from . import views


urlpatterns = [
    path('',views.project_list,name='project_list'),
    path('add/',views.add_project,name='add_project'),
    path('<int:pk>/edit/',views.edit_project,name='edit_project'),
    path('<int:pk>/delete/',views.delete_project,name='delete_project'),
    path('<int:project_id>/upload/',views.upload_document,name='upload_document'),
    path('<int:pk>/',views.project_detail,name='project_detail'),
]
