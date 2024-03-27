from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.get_list),
    path('list/filtered-list', views.filtered_list),
    path('list/<int:id>', views.single_list_details),
    path('list/create-list/', views.create_list),
    path('list/update-list/<int:id>', views.update_list),
    path('list/delete-list/<int:id>', views.delete_list),

    path('tag/', views.tag_list),
    path('tag/create-tag/', views.create_tag),
    path('tag/update-tag/<int:id>', views.update_tag),
    path('tag/delete-tag/<int:id>', views.delete_tag),
]
