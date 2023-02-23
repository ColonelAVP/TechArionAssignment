from django.urls import path
from accounts.controllers.user_operations import UserController

urlpatterns = [
    path("get_all_users/", UserController.get_all_users, name="get-all-user"),
]
