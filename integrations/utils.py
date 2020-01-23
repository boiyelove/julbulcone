import faker
import random
from django.contrib.auth import get_user_model
from .models import IntegrationVerification, Integration

fake = faker.Faker()
User = get_user_model()

def create_dummy_data():
	user = User.objects.get(id=1)
	for i in range(1,20):
		Integration.objects.create(user = user, domain_name=fake.domain_name(), active =random.getrandbits(1))
		# int = IntegrationVerification.objects.create(user = user, domain_name=fake.domain_name(), active =random.choices(True, False))