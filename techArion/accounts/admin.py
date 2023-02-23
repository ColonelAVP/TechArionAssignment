from django.contrib import admin
from .models import User, UserProfile, UserLoginOtp, UserCart, UserCartProduct

# Register your models here.
admin.site.register(User)
admin.site.register(UserProfile)
