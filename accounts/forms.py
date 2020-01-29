from django import forms
from allauth.account.forms import SignupForm
from .models import JUser


class SignUpForm(SignupForm):
	full_name = forms.CharField()
	password2 = forms.CharField(widget=forms.PasswordInput, label='Repeat Password')


	def clean_email(self):
		email = self.cleaned_data.get('email', None)
		if JUser.objects.filter(email = email):
			raise forms.ValidationError('User with this email address already exists')
		return email

	def create_user(self):
		user = JUser.objects.create_user(username = self.cleaned_data.get('username'),
			full_name = self.cleaned_data.get('full_name'),
			email = self.cleaned_data.get('email'))
		user.set_password(self.cleaned_data.get('password1'))
		return user.save() 

class ProfileForm(forms.ModelForm):
	class Meta:
		model = JUser
		fields = ['full_name', 'email']


	def clean_email(self):
		email = self.cleaned_data.get('email', None)
		if JUser.objects.filter(email = email):
			raise forms.ValidationError('User with this email address already exists')
		return email
