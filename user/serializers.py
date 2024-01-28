from rest_framework import serializers
from django.contrib.auth.models import User
from user.models import UserProfile


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    email = serializers.CharField(source='user.email')
    password = serializers.CharField(source='user.password', write_only=True)
    avatar = serializers.CharField(required=False)
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'points', 'avatar')

    def create(self, validated_data):
        # Extract user-related data
        user_data = validated_data.pop('user', {})
        username = user_data.get('username')
        email = user_data.get('email')
        password = user_data.get('password')
        # Create or get the User instance
        user, created = User.objects.get_or_create(username=username, email=email)
        if created:
            user.set_password(password)
            user.save()

        # Create the UserProfile instance
        profile = UserProfile.objects.create(user=user, **validated_data)

        return profile


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    password = serializers.CharField(source='user.password')

    class Meta:
        model = UserProfile
        fields = ('username', 'password')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        pass
