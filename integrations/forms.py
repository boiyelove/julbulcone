from django import forms
from .models import Integration


class DomainForm(forms.ModelForm):
	class Meta:
		model = Integration
		fields = ['domain_name']

	def clean_domain_name(self):
		domain = self.cleaned_data.get('domain', None)
		if domain:
			domain_exist = IntegrationVerification.ppbjects.filter(domain=domain)
			domain_exist1 = Integration.objects.filter(domain = domain)
		if domain_exist or domain_exist1:
			raise forms.ValidationError('Sorry website has already been registered by you or another user')
		return domain
			