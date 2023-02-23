from rest_framework import serializers
from .models import User, UserCart
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "phone_number",
            "email",
            "is_customer",
            "is_admin",
        ]
