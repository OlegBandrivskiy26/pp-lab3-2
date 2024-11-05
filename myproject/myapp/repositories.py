from .models import Customer, Car, Supplier, Shipment, Order, Manager, Payment, PaymentMethod

class CustomerRepository:
    def get_all_customers(self):
        return Customer.objects.all()
    
    def get_customer_by_id(self, customer_id):
        return Customer.objects.get(pk=customer_id)
    
    def create_customer(self, data):
        return Customer.objects.create(**data)
    
    def update_customer(self, customer_id, data):
        customer = Customer.objects.get(pk=customer_id)
        for attr, value in data.items():
            setattr(customer, attr, value)
        customer.save()
        return customer
    
    def delete_customer(self, customer_id):
        Customer.objects.get(pk=customer_id).delete()

# Аналогічні класи-репозиторії створіть для інших моделей
