from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProfileForm, SignUpForm

# Create your views here.

class LoginRequiredMixin(LoginRequiredMixin):
	login_url = reverse_lazy('account_login')


class AccountProfileView(LoginRequiredMixin, FormView):
	form_class = ProfileForm
	success_url = reverse_lazy('edit-profile')
	template_name = 'forms.html'
	extra_context = {'form_title': "Edit Profile"}

	def get_initial(self):
		return {'full_name' : self.request.user.full_name, 'email': self.request.user.email}


def signup(request):
	if request.user.is_authenticated:
		return redirect(reverse_lazy('list-domains'))
	form = SignUpForm(request.POST or None)
	if form.is_valid():
		user = form.create_user()
		return redirect(reverse_lazy('account_login'))
	return render(request, 'account/signup.html', {'form_title': "Edit Profile", 'form': form})

