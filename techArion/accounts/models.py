from django.db.models import Model
from django.db.models import (
    IntegerField,
    CharField,
    TextField,
    BooleanField,
    EmailField,
    DateField,
    OneToOneField,
    ForeignKey,
    ManyToManyField,
    CASCADE,
    FloatField,
)
from product.models import ProductMain, ProductImage


# Create your models here.
class User(Model):
    phone_number = CharField(max_length=10, unique=True)
    email = EmailField(unique=True)
    is_customer = BooleanField(default=True)
    is_admin = BooleanField(default=False)

    def __str__(self):
        return str(self.email)


gender_choices = (
    ("M", "Male"),
    ("F", "Female"),
    ("O", "Others"),
)


class UserProfile(Model):
    owner = OneToOneField(User, on_delete=CASCADE)
    name = TextField(max_length=15)
    dob = DateField()  # It must be a YYYY-MM-DD format
    gender = TextField(choices=gender_choices)


class UserLoginOtp(Model):
    owner = ForeignKey(User, on_delete=CASCADE)
    otp = IntegerField()
    active = BooleanField(default=False)


status_choices = (
    ("P", "pending"),
    ("C", "completed"),
)


class UserCartProduct(Model):
    owner = ForeignKey(User, on_delete=CASCADE)
    product = ForeignKey(ProductMain, on_delete=CASCADE)
    status = TextField(choices=status_choices)


class UserCart(Model):
    owner = OneToOneField(User, on_delete=CASCADE)
    products = ManyToManyField(UserCartProduct)
    price = FloatField(max_length=10)
