from django import forms
from allauth.account.forms import SignupForm
from .models import JUser


class SignUpForm(SignupForm):
	full_name = forms.CharField()
	# password2 = forms.CharField(widget=forms.PasswordInput, label='Repeat Password')


