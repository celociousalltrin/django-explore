from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.get_list),
    path('list/filtered-list', views.get_list),
    path('list/<int:id>', views.single_list_details),
    path('list/create-list/', views.create_list),
    path('list/update-list/<int:id>', views.update_list),
    path('list/delete-list/<int:id>', views.delete_list),
]
