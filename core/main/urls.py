from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user_page/<int:id>/', views.user_page, name='user_page'),
    path('login/', views.login_request, name='login'),
    path('register/',views.register_request, name='register'),
    path('logout/', views.logout_request, name='logout'),
    path('delete_post/', views.delete_post, name='delete_post')
]