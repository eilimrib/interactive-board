from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models


class Card(models.Model):
    title = models.CharField(max_length=50)
    value = models.IntegerField(default=0)
    content = models.CharField(max_length=500)