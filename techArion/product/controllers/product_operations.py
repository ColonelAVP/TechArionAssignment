from rest_framework.decorators import api_view
from product.repositories.product import create_product, get_product

from accounts.helpers.base import (
    BadRequestJSONResponse,
    SuccessJSONResponse,
    UnauthorizedJSONResponse,
    NotFoundJSONResponse,
)


class ProductController:
    @staticmethod
    @api_view(["POST"])
    def create_product(request):
        post_data = request.data
        success, response = create_product(post_data=post_data)
        if not success:
            return BadRequestJSONResponse(message=response)
        return SuccessJSONResponse(response)

    @staticmethod
    @api_view(["GET"])
    def get_products(request):
        success, response = get_product()
        if not success:
            return BadRequestJSONResponse(message=response)
        return SuccessJSONResponse(response)
