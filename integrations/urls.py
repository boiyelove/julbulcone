from django.urls import path
from .views import AddDomainFView, DomainListView

urlpatterns = [
	path('add_domain/', AddDomainFView.as_view(), name='add-domain' ),
	path('domains/', DomainListView.as_view(), name='list-domain' ),
]