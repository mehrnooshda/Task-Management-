from django.shortcuts import render
from django.contrib.auth import authenticate, login
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from common.views import BaseViewSet
from user.serializers import UserInfoSerializer, LoginSerializer, ProfileSerializer, \
    RegisterSerializer
from rest_framework import viewsets, mixins, status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import action
from .models import UserProfile


class UserViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, BaseViewSet):
    # mixins are also used in root of the project /api in order to create a comprehensive documentation
    serializer_class = UserInfoSerializer
    permission_classes = [IsAuthenticated]  # this is default

    serializer_classes = {
        'register': RegisterSerializer,
        'login': LoginSerializer,
        'get_profile': ProfileSerializer
    }

    @action(detail=False, methods=['post'], url_path='register', url_name='register', permission_classes=[AllowAny])
    def register(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        user_profile = serializer.save()
        data = {
            'username': user_profile.user.username,
            'email': user_profile.user.email,
            'points': user_profile.points,
            'response': 'Account has been created successfully'
        }

        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'], url_path='login', url_name='login', permission_classes=[AllowAny])
    def login(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            username=serializer.data['username'],
            password=serializer.data['password']
        )
        if user is not None:
            login(request, user)
            return Response(data={'detail': True, 'redirect_url': 'felan nemidunam'}, status=status.HTTP_200_OK)
        return Response(data={'detail': False}, status=status.HTTP_404_NOT_FOUND)
