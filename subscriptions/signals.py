from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import JUser
from.models import JUserSubscription

@receiver(post_save, sender=JUser)
def set_verification_hash(sender, instance, created, *args, **kwargs):
	if created:
			JUserSubscription.object.create(user = instance)