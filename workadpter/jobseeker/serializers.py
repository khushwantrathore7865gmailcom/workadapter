from rest_framework import serializers
import datetime
from user_coustom.models import User_custom

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_custom
        fields = ( 'username','email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_custom
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User_custom.objects.create_user(**validated_data, iscandidate=True, last_login=datetime.datetime.now())

        return user