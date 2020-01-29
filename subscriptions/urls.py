from django.urls import path
from . import views

urlpatterns = [
	path('subscription/', views.view_subscriptions, name='subscription-view' ),
	path('process-payment/', views.process_payment, name='process-subscription'),
	path('payment-done/', views.payment_done, name='payment-done'),
	path('payment-cancelled/', views.payment_cancelled, name='payment-cancelled'),
]