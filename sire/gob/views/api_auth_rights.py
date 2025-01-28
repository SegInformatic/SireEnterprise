from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from gob.models import Right


@api_view(['GET'])
def get_user_rights(request):
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return Response({"error": "Token is missing"}, status=status.HTTP_401_UNAUTHORIZED)

    token = auth_header.split(' ')[1]

    try:
        token_obj = Token.objects.get(key=token)
        user = token_obj.user

        group_rights = Right.objects.filter(groupright__users=user).values_list('name', flat=True)

        user_data = {
            "user_id": user.id,
            "rights": list(group_rights),
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email
        }

        return Response(user_data, status=status.HTTP_200_OK)

    except Token.DoesNotExist:
        return Response({"error": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED)

    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
