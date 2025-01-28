from django.db import models
from django.contrib.auth.models import User

from gob.models.rights import Right


class GroupRight(models.Model):
    name = models.CharField(max_length=100)
    rights = models.ManyToManyField(Right)
    users = models.ManyToManyField(User, related_name='group_rights')

    def __str__(self):
        return self.name
