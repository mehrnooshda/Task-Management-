from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from common.views import BaseViewSet
from user.serializers import UserInfoSerializer, LoginSerializer, ProfileSerializer, \
    RegisterSerializer
from rest_framework import viewsets, mixins, status
from rest_framework_simplejwt.tokens import RefreshToken, Token
from rest_framework.decorators import action
from .models import UserProfile


class UserViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, BaseViewSet):
    # mixins are also used in root of the project /api in order to create a comprehensive documentation
    serializer_class = UserInfoSerializer
    permission_classes = [IsAuthenticated]  # this is default
    queryset = UserProfile.objects.all()

    serializer_classes = {
        'profile': ProfileSerializer
    }

    @action(
        detail=False,
        methods=['POST'],
        url_path='register',
        url_name='register',
        permission_classes=[AllowAny],
        serializer_class=RegisterSerializer
    )
    def register(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        if UserProfile.objects.filter(user__username=request.data['username']):
            return Response({'detail': 'User already exists'}, status=status.HTTP_409_CONFLICT)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False,
            methods=['POST'],
            url_path='login',
            url_name='login',
            permission_classes=[AllowAny],
            serializer_class=LoginSerializer)
    def login(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            username=serializer.data['username'],
            password=serializer.data['password']
        )
        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            return Response(data={'detail': True, 'access_token': access_token, 'redirect_url': 'felan nemidunam'},
                            status=status.HTTP_200_OK)
        return Response(data={'detail': False}, status=status.HTTP_404_NOT_FOUND)

    # @action(detail=False,
    #         methods=['GET'],
    #         url_name='user-profile',
    #         # url_path='an',
    #         permission_classes=[IsAuthenticated],
    #         serializer_class=ProfileSerializer)
    # def profile(self, request, pk=None, *args, **kwargs):
    #     print(pk, request.data)
    #     print('saaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaag')
    #     user_profile = get_object_or_404(UserProfile, pk=1)
    #     print(type(user_profile))
    #     # return Response({'detail': True, 'data': user_profile})
    #     return Response(self.serializer_class(user_profile).data)
