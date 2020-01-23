from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.
class JUser(AbstractUser):
	# user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	first_name = None
	last_name = None
	full_name = models.CharField(max_length=120)