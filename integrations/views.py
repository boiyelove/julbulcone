from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import FormView
from .models import Integration
from .forms import DomainForm

# Create your views here.

class AddDomainFView(SuccessMessageMixin, FormView):
	form_class = DomainForm
	template_name = 'ajax_form.html'
	success_url = 'Your domain name has been added successfully'
	success_url = reverse_lazy('list-domain')
	extra_context = {'urlname': 'add-domain'}



class DomainListView(ListView):
	template_name = 'domain_grid.html'
	queryset = Integration.objects.all()
