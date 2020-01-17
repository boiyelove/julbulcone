from django import forms
from .models import Integration


class DomainForm(forms.ModelForm):
	class Meta:
		model = Integration
		fields = ['domain']
