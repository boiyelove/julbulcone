import domcheck
from django.db import models
from django.conf import settings
from model_utils.models import TimeStampedModel
# Create your models here.


class Integration(TimeStampedModel):
	domain = models.URLField(unique=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	active = models.BooleanField(default = False)


class Video(TimeStampedModel):
	source_page = models.URLField()
	youtube_url = models.URLField()
	link = models.FileField(upload_to='videos/')
	active = models.BooleanField(default = True)

class IntegrationVerification(TimeStampedModel):
	domain = models.URLField(unique=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	verification_hash = models.CharField(max_length=160)
	verfied = models.BooleanField(default=False)

	def verify(self):
		if domcheck.check(self.domain, 'julbul-verification', self.code, strategies='meta_tag'):
			if not self.verified:
				self.verified = True
				self.save()
			return True
		return False

