from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser


from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.
class User_custom(AbstractUser):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=250, unique=True, null=True)
    # name = models.CharField(max_length=250,blank=True)
    email = models.EmailField(max_length=254)
    # password = models.CharField(max_length=32,widget=forms.PasswordInput)
    password = models.CharField(max_length=32)
    last_login = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    # user_permissions = models.CharField(blank=True,null=True)
    # confirmpass = models.CharField(max_length=32, blank=True)
    iscandidate = models.BooleanField(default=False)
    isemployeer = models.BooleanField(default=False)

    def __str__(self):
        return self.username


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     print(instance)
#     if created:
#         t = Token.objects.create(user=instance)
#         t.save()


