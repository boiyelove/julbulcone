from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import ProfileForm

# Create your views here.
class AccountProfileView(FormView):
	form_class = ProfileForm
	success_url = reverse_lazy('edit-profile')
	template_name = 'forms.html'
	extra_context = {'form_title': "Edit Profile"}
	
	def get_initial(self):

		return {'full_name' : self.request.user.full_name, 'email': self.request.user.email}
