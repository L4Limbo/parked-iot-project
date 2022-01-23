from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class User(AbstractUser):
    blueCard = models.ImageField(null=True, default="avatar.svg")
    usercardcode = models.CharField(db_column='userCardCode', max_length=50, blank=True, null=True)
    uservalid = models.BooleanField(blank=True, null=True)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
