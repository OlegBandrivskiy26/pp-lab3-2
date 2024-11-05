from django.contrib import admin
from .models import Customer, Car, Supplier, Shipment, Order, Manager, Payment, PaymentMethod

admin.site.register(Customer)
admin.site.register(Car)
admin.site.register(Supplier)
admin.site.register(Shipment)
admin.site.register(Order)
admin.site.register(Manager)
admin.site.register(Payment)
admin.site.register(PaymentMethod)
