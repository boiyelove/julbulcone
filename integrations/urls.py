from django.urls import path
from . import views

urlpatterns = [
	path('', views.DomainListView.as_view(), name='' ),
	path('add_domain/', views.add_domain, name='add-domain' ),
	path('domains/', views.DomainListView.as_view(), name='list-domain' ),
	path('domains/verify/<int:id>/', views.verify_domain, name='verify-domain' ),
	path('domains/<int:pk>/', views.DomainDetailView.as_view(), name='view-domain' ),
]
