from django.urls import path
from product.controllers.product_operations import ProductController

urlpatterns = [
    path("create_product/", ProductController.create_product, name="create-product"),
    path("get_products/", ProductController.get_products, name="get-products"),
]
