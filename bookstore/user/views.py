"""
User View 
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from django.contrib.auth.models import User


from .serializers import UserRegisterSerializer


class UserRegisterView(APIView):
    """
    User creation view 
    """
    def post(self, request):
        """
        creating user account
        """
        ser_data = UserRegisterSerializer(data=request.data)
        if ser_data.is_valid():
            # create is function in serializer.py that creates user
            ser_data.create(ser_data.validated_data)

            return Response(ser_data.data, status =status.HTTP_201_CREATED )
        return Response(ser_data.errors , status = status.HTTP_400_BAD_REQUEST)
            