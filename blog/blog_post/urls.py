from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.api_blog_post_create),
    path('test/', views.test.as_view()),
    # path('blog_detail/<int:pk>/',views.api_blog_post_detail),
    # path('update/<int:pk>/',views.api_blog_post_update),
    # path('delete/<int:pk>/',views.api_blog_post_delete),
    # path('list',views.ApiBlogListView.as_view()),
]