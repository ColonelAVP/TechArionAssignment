from rest_framework.decorators import api_view
from accounts.repositories.user import get_all_users
from accounts.helpers.base import (
    BadRequestJSONResponse,
    SuccessJSONResponse,
    UnauthorizedJSONResponse,
    NotFoundJSONResponse,
)


class UserController:
    @staticmethod
    @api_view(["GET"])
    def get_all_users(request):
        success, response = get_all_users()
        if not success:
            return BadRequestJSONResponse(message=response)
        return SuccessJSONResponse(response)
