from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView
from accounts.views import LoginRequiredMixin
from .models import Integration
from .forms import DomainForm


# Create your views here.

class AddDomainFView(LoginRequiredMixin, SuccessMessageMixin, FormView):
	form_class = DomainForm
	template_name = 'ajax_form.html'
	success_message = 'Your domain name has been added successfully'
	success_url = reverse_lazy('list-domain')
	extra_context = {'urlname': 'add-domain'}

	def form_valid(self, form):
		print('form is', form)
		print('request is', self.request.POST)
		domain = form.cleaned_data.get('domain', None)
		int_ver, created = IntegrationVerification.objects.get_or_create(domain = domain)
		return render(self.request, 'domain_verification.html', {'website_item': int_ver})
		# return super(AddDomainFView, self).form_valid(form)

	def form_invalid(self, form):
		print('form is', form)
		print('request is', self.request.POST)
		return render(self.request, self.template_name, {'form': form})



class DomainListView(LoginRequiredMixin, ListView):
	template_name = 'domain_grid.html'
	context_object_name = 'website_list'
	
	def get_queryset(self):
		return  Integration.objects.filter(user=self.request.user)[:11]

def verify_domain(self, request, *args, **kwargs):
		pk = kwargs.get('pk', None)
		if pk:
			int_ver = Integration.objects.filter(id = pk)
			if  int_ver.verify():
				return JsonResponse({'verified':True})
			else:
				return JsonResponse({'verified':False})
		return Http404

class DomainDetailView(LoginRequiredMixin, DetailView):
	template_name = 'domain_detail.html'
	pk_or_slug = 'pk'
	model =  Integration
	context_object_name = 'website'
	