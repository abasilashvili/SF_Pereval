from django.urls import path
from .views import *

user_list = UserViewSet.as_view({'get': 'list', 'post': 'create'})
user_details = UserViewSet.as_view({'get': 'retrieve', 'put': 'update'})
urlpatterns = [
    path('', api_root),
    path('submitData/', PerevalCreateView.as_view(), name='submitData'),
    path('submitData/<int:pk>/', PerevalDetailView.as_view()),
    path('user/', user_list, name='user'),
    path('user/<int:pk>', user_details)
]