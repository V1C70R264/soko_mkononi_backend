from rest_framework import serializers
from .models import CustomUser  # Make sure this is your custom user model

# 1. Registration Serializer
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    phone_number = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'phone_number')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            phone_number=validated_data.get('phone_number', '')
        )
        return user

# 2. User/Profile Serializer
class UserSerializer(serializers.ModelSerializer):
    profile_image = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'phone_number', 'first_name', 'last_name', 'profile_image']
        read_only_fields = ['id', 'username', 'email']  # Adjust as needed