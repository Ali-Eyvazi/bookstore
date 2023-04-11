"""
user serializer 
"""
import re
from rest_framework import serializers
from .models import User


def clean_email(value):
    """
    verify email by regex and other conditions
    """
    if 'admin' in value:
        raise serializers.ValidationError(" admin can't be in the email ")
    if not re.search(r"^[A-Za-z0-9_!#$%&'*+\/=?`{|}~^.-]+@[A-Za-z0-9.-]+$", value):
        print(f"The email address {value} is not valid")
        return False
    return value


class UserRegisterSerializer(serializers.ModelSerializer):
    """
    user serializer , using model serializer, validating data that are comming from user
    """
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        """
        defining details of serializer
        """
        model = User
        fields = ('email', 'phone_number',
                  'full_name', 'password', 'password2')

        extra_kwargs = {'password': {'write_only': True},
                        'email': {'validators': (clean_email,)}}

    def create(self, validated_data):
        del validated_data['password2']
        return User.objects.create_user(**validated_data)

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError('passwords are not match')

        return attrs
