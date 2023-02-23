from product.models import ProductImage
from rest_framework.serializers import ModelSerializer


class ProductSerializer(ModelSerializer):
    class Meta:
        model = ProductMain
        fields = [
            "image",
            "title",
            "description",
            "price",
        ]
