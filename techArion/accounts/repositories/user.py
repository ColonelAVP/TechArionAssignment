from accounts.models import User
from accounts.serializer import UserSerializer
import json


def get_all_users():
    """
    get_all_user() returns all the users
    """
    users = User.objects.all()
    serialized_data = UserSerializer(users, many=True).data
    print(serialized_data)
    final_user_data = json.dumps(serialized_data)
    print(final_user_data)
    if not final_user_data:
        return False, "Users not Found"
    return True, final_user_data
