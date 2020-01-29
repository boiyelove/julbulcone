from django.contrib import admin
from  .models import Subscription, JUserSubscription, Order

# Register your models here.
admin.site.register(Subscription)
admin.site.register(JUserSubscription)
admin.site.register(Order)