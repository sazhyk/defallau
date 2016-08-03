from django.db import models
from django.contrib.auth.models import User


class MyProfile(models.Model):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='my_profile')
