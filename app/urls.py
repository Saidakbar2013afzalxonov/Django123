

from django.urls import path
from . import views

urlpatterns=[
    path("",views.UserListView.as_view(),name='user_list'),
    path("user/<slug:slug>/", views.UserDetailView.as_view(), name='user_view'),
    path("user/create",views.UserCreateView.as_view(),name='create_user'),
    path("user/update/<slug:slug>/", views.UserUpdateView.as_view(), name='update_user'),
    path("user/delete/<slug:slug>/", views.UserDeleteView.as_view(), name='delete_user'),
]