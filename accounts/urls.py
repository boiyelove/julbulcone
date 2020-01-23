from django.urls import path
from .import views
urlpatterns = [

	path('account/', views.AccountProfileView.as_view(), name='edit-profile'),
	]
