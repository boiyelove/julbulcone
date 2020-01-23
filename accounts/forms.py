from django import forms
from allauth.account.forms import SignupForm
from .models import JUser


class SignUpForm(SignupForm):
	full_name = forms.CharField()
	# password2 = forms.CharField(widget=forms.PasswordInput, label='Repeat Password')

class ProfileForm(forms.ModelForm):
	class Meta:
		model = JUser
		fields = ['full_name', 'email']


	def clean_email(self):
		email = self.cleaned_data.get('email', None)
		if JUser.objects.filter(email = email):
			raise forms.ValidationError('User with this email address already exists')
		return email
