from django.urls import path
from .views import SubscriptionTemplateView

urlpatterns = [
	path('subscription/', SubscriptionTemplateView.as_view(), name='subscription-view' ),

]