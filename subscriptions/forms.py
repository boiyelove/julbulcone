from django import forms
from .models import Subscription




class SubscriptionForm(forms.Form):
	plans = forms.ChoiceField(choices=[(sub.id, sub.title) for sub in Subscription.objects.all()])
	# cycle = forms.ChoiceField(choices=[(1,'1 Month'), (2, '3 Months'), (3, '6 Months')])