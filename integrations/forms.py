import validators
from django import forms
from .models import Integration



class DomainForm(forms.Form):
	domain_name = forms.CharField(max_length=255)

	def __init__(self, user_sub, *args, **kwargs):
		super(DomainForm, self).__init__(*args, **kwargs)
		self.user = user_sub

	def clean_domain_name(self):
		domain = self.cleaned_data.get('domain_name')
		print('domain name is ', domain)
		if domain:
			if validators.domain(domain) is not True:
				raise forms.ValidationError('Enter a valid domain name')
			if not self.user_sub.can_add_domains():
				raise forms.ValidationError('You have used up all your slots, please upgrade')
			domain_exist1 = Integration.objects.filter(domain_name = domain)
			if domain_exist1:
				raise forms.ValidationError('Sorry website has already been registered by you or another user')
		return domain
			
	def create_domain(self, user):
		return Integration.objects.create(domain_name = self.cleaned_data.get('domain_name'),
			user = user)