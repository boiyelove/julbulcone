from django.db import models
from django.conf import settings
from model_utils.models import TimeStampedModel
from integrations.models import Integration

# Create your models here.
# BILLING_UNITS = (('M', 'Monthly'),)

class Subscription(TimeStampedModel):
	title = models.CharField(max_length=120)
	domain_limit = models.PositiveIntegerField(default=1)
	price = models.PositiveIntegerField(default=5)
	active = models.BooleanField(default=True)
	# billing_cycle = models.PositiveIntegerField(default=1)
	# billing_unit = models.CharField(max_length=1, choices=BILLING_UNITS, default='M')

class JUserSubscription(TimeStampedModel):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	subscription = models.ForeignKey('Subscription', null=True, blank=True, on_delete=models.SET_NULL)
	active = models.BooleanField(default=False)
	end_date = models.DateTimeField(null=True)
	start_date = models.DateTimeField(null=True)


	def activate(self, subscription, months=None):
		self.subscription = subscription
		return self.save()

	def deactivate(self):
		self.subscription, self.end_date, self.start_date = None
		return self.save()

	def get_domain_limit(self):
		if self.subscription:
			return self.subscription.domain_limit
		return 0

	def get_remaining_slots(self):
		if self.subscription:
			return self.subscription.domain_limit - Integration.objects.filter(user = self.user).count()
		return 0 - Integration.objects.filter(user = self.user).count()

	def can_add_domains(self):
		if self.get_remaining_slots() > 0:
			return True
		return False

class Order(TimeStampedModel):
	subscription = models.ForeignKey('Subscription', on_delete=models.SET_NULL, null=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

