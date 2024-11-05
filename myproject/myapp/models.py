from django.db import models

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    manager = models.ForeignKey('Manager', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"


class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.DateField()
    engine_volume = models.FloatField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mileage = models.IntegerField()
    VIN = models.CharField(max_length=255)
    description = models.TextField()
    country = models.CharField(max_length=255)
    imported_date = models.DateField()
    shipment = models.ForeignKey('Shipment', on_delete=models.SET_NULL, null=True, related_name='cars')

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year.year})"


class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    contact_info = models.TextField()
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Shipment(models.Model):
    shipment_id = models.AutoField(primary_key=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    shipment_date = models.DateField()
    arrival_date = models.DateField()
    shipping_status = models.CharField(max_length=255)

    def __str__(self):
        return f"Shipment #{self.shipment_id} - {self.shipping_status}"


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    order_date = models.DateField()
    status = models.CharField(max_length=255)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    shipment = models.ForeignKey(Shipment, on_delete=models.SET_NULL, null=True)
    manager = models.ForeignKey('Manager', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Order #{self.order_id} - {self.customer.first_name} {self.customer.last_name}"


class Manager(models.Model):
    manager_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    hiring_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    shipment = models.ForeignKey(Shipment, on_delete=models.SET_NULL, null=True)
    amount = models.FloatField()
    payment_method = models.ForeignKey('PaymentMethod', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Payment #{self.payment_id} - ${self.amount}"


class PaymentMethod(models.Model):
    payment_method_id = models.AutoField(primary_key=True)
    cash = models.FloatField()
    card = models.FloatField()
    recalculation = models.FloatField()
    partial_payment = models.FloatField()

    def __str__(self):
        return f"PaymentMethod #{self.payment_method_id}"
