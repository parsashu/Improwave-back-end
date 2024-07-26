from django.urls import path
from . import views

urlpatterns = [
    # path('login/', views.login_view, name='login'),
    # path('register/', views.register_view, name='register'),
    # path('token/', views.test_token, name='test-token'),
    path('users/', views.user_list, name='user-list'),
    path('users/<int:pk>/', views.user_detail, name='user-detail'),

]