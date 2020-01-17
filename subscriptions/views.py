from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class SubscriptionTemplateView(TemplateView):
	template_name = 'subscriptions.html'
