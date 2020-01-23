from django.db import models
from django.conf import settings
from model_utils.models import TimeStampedModel

# Create your models here.

class Subscription(TimeStampedModel):
	title = models.CharField(max_length=120)
	domain_limit = models.PositiveIntegerField(default=1)
	active = models.BooleanField(default=True)

class JUserSubscription(TimeStampedModel):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	subscription = models.ForeignKey(Subscription, null=True, blank=True, on_delete=models.SET_NULL)
	active = models.BooleanField(default=False)
	end_date = models.DateTimeField(null=True)
	start_date = models.DateTimeField(null=True)