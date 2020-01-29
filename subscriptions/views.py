from django.contrib import messages
from django.conf import settings
from decimal import Decimal
from paypal.standard.forms import PayPalPaymentsForm
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Subscription, Order
from .forms import SubscriptionForm
# from .forms import CartForm, CheckoutForm

# Create your views here.

class SubscriptionTemplateView(TemplateView):
	template_name = 'subscriptions.html'

def checkout(request):
	pass

def view_subscriptions(request):
	form = SubscriptionForm(request.POST or None)
	if form.is_valid():
			request.session['sub_id'] = request.POST.get('plan')
			return redirect('process_subscrition')

	return render(reques, 'subscriptions.html', {'form': form, 'subscriptions':Subscription.objects.all()})

def process_payment(request):
	sub_id = request.session.get('sub_id')
	host = request.get_host()
	sub = Subscription.objects.get(id=sub_id)

	order_id = request.session.get('order_id')
	order = get_object_or_404(Order, id=order_id)
	host = request.get_host()
	billing_cycle = 1
	billing_cycle_unit = 'M'
	paypal_dict = {
	"cmd": "x_xclick-subscriptions",
	'business': settings.PAYPAL_RECEIVER_EMAIL,
	"a3": sub.price,
	"p3": sub.billing_cycle, # duration of each unit (depends on unit)
	"t3": billing_cycle_unit, # duration unit ("M for Month")
	"src": "1",  # make payments recur
	"sra": "1", # reattempt payment on payment error
	"no_note": "1",
	"item_name": 'Julbule Clone - %s' % sub.title,
	'currency_code': 'USD',
	'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
	'return_url': 'http://{}{}'.format(host, reverse('payment:done')),
	'cancel_return': 'http://{}{}'.format(host, reverse('payment:canceled')),
	}

	form = PayPalPaymentsForm(initial=paypa_dict, button_type="subscribe")
	return render(request, process_subscrition.html, locals())