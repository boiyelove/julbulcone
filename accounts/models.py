from django.db import models
from django.conf import settings


# Create your models here.
class JUser(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	full_name = models.CharField(max_length=120)