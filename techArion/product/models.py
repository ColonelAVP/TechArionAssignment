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
    FloatField,
    CASCADE,
    ImageField,
)
import random


def generate_product_id():
    product_id = "".join(
        [random.choice("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ") for i in range(6)]
    )
    return product_id


# Create your models here.
class ProductMain(Model):
    title = TextField(max_length=50)
    description = TextField(max_length=200)
    unique_id = CharField(max_length=6, default=generate_product_id, unique=True)
    price = FloatField(max_length=10)

    def __str__(self):
        return str(self.title)


# def get_images(product):
#     return f"product_images/{product}"


class ProductImage(Model):
    product = ForeignKey(ProductMain, on_delete=CASCADE)
    image = ImageField(upload_to="product_images/")

    def __str__(self):
        return str(self.product)
