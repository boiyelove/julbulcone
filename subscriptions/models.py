from django.db import models
from model_utils.models import TimeStampedModel

# Create your models here.

class Subscription(TimeStampedModel):
	title = models.CharField(max_length=120)
	domain_limit = models.PositiveIntegerField(default=1)
	active = models.BooleanField(default=True)