from django.urls import path
from .views import AddDomainFView, DomainListView, verify_domain

urlpatterns = [
	path('add_domain/', AddDomainFView.as_view(), name='add-domain' ),
	path('domains/', DomainListView.as_view(), name='list-domain' ),
	path('domains/<int:id>/', verify_domain, name='verify-domain' ),
]