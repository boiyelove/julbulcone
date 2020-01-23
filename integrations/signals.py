from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import IntegrationVerification

@receiver(pre_save, sender=IntegrationVerification)
def set_verification_hash(sender, instance, **kwargs):
	instance.set_hash()