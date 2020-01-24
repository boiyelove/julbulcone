from django.urls import path
from .views import AddDomainFView, DomainListView, verify_domain, DomainDetailView

urlpatterns = [
	path('', DomainListView.as_view(), name='' ),
	path('add_domain/', AddDomainFView.as_view(), name='add-domain' ),
	path('domains/', DomainListView.as_view(), name='list-domain' ),
	path('domains/verify/<int:id>/', verify_domain, name='verify-domain' ),
	path('domains/<int:pk>/', DomainDetailView.as_view(), name='view-domain' ),
]
