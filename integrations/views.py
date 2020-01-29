from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView
from accounts.views import LoginRequiredMixin
from subscriptions.models import JUserSubscription
from .models import Integration
from .forms import DomainForm


# Create your views here.
@login_required
def add_domain(request):
	user_sub = JUserSubscription.objects.get(user = request.user )
	form = DomainForm (request.POST or None, user_sub=user_sub)
	if form.is_valid():
		integration = form.create_domain(request.user)
		messages.success(request, 'Website added succesfully')
		return HttpResponse(reverse_lazy('list-domain'), status=301)
	return render(request, 'ajax_form.html', {'form':form, 'urlname': 'add-domain'} )


class DomainListView(LoginRequiredMixin, ListView):
	template_name = 'domain_grid.html'
	context_object_name = 'website_list'
	
	def get_queryset(self):
		return  Integration.objects.filter(user=self.request.user)

	def get_context_data(self,**kwargs):
		juser_sub,created = JUserSubscription.objects.get_or_create(user=self.request.user)
		kwargs['remaining_slots'] =  juser_sub.get_remaining_slots()
		kwargs['total_domain_count'] = juser_sub.get_domain_limit()
		return super().get_context_data(**kwargs)




def verify_domain(self, request, *args, **kwargs):
	# pk = kwargs.get('pk', None)
	# if pk:
	# 	int_ver = Integration.objects.filter(id = pk)
	# 	if  int_ver.verify():
	# 		return JsonResponse({'verified':True})
	# 	else:
	# 		return JsonResponse({'verified':False})
	return Http404


class DomainDetailView(LoginRequiredMixin, DetailView):
	template_name = 'domain_detail.html'
	pk_or_slug = 'pk'
	model =  Integration
	context_object_name = 'website'
