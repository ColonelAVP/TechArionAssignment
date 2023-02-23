from product.models import ProductMain, ProductImage
from product.serializer import ProductSerializer

# from accounts.serializer import UserSerializer
import json


def create_product(post_data):
    print(type(post_data))
    title = post_data.get("title")
    description = post_data.get("description")
    price = post_data.get("price")
    product_data = ProductMain.objects.filter(title=title)
    if product_data.first():
        return True, "Product Already Exists"
    product = ProductMain.objects.create(
        title=title,
        description=description,
        price=price,
    )
    product.save()
    return True, "Product Created Successfully"


def get_product():
    product = ProductMain.objects.all()
    product_images = ProductImage.objects.all()
    serialized_products = ProductSerializer(product_images)
    print(serialized_products)
    final_product_data = json.dumps(serialized_products)
    if not final_product_data:
        return False, "No product exists"
    return True, final_product_data
