from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password


class Avatar(models.Model):
    picture = models.CharField(max_length=100000)
    min_points_to_earn = models.IntegerField()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ForeignKey(Avatar, on_delete=models.CASCADE, null=True)
    points = models.PositiveIntegerField(default=0)

    # @property
    # def get_username(self):
    #     return self.user.username if self.user else None
