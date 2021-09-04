from django.urls import path
from apps.postApp import views

urlpatterns = [
    path('', views.MyFormAddShowView.as_view(), name="add"),
    path('delete/<int:id>/', views.delete_data, name="deletedata"),
    path('<int:id>/', views.update_data, name="updatedata"),
    path('posts/', views.MyFormAddPost.as_view(), name="add_post"),
    path('delete_post/<int:id>/', views.delete_post, name="delete_post"),
    path('update_post/<int:id>/', views.update_post, name="update_post"),
    path('comment/', views.FormAddComment.as_view(), name="add_comment"),
    path('delete_comment/<int:id>/', views.delete_comment, name="delete_comment"),
    path('update_comment/<int:id>/', views.update_comment, name="update_comment"),
]