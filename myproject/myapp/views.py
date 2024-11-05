from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Avg, Sum
from .repositories import CustomerRepository
from .serializers import CustomerSerializer

class CustomerViewSet(viewsets.ViewSet):
    repository = CustomerRepository()
    
    def list(self, request):
        customers = self.repository.get_all_customers()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        customer = self.repository.get_customer_by_id(pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            customer = self.repository.create_customer(serializer.validated_data)
            return Response(CustomerSerializer(customer).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            customer = self.repository.update_customer(pk, serializer.validated_data)
            return Response(CustomerSerializer(customer).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        self.repository.delete_customer(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReportView(APIView):
    def get(self, request):
        total_orders = Order.objects.count()
        avg_order_value = Order.objects.aggregate(Avg('total_price'))
        total_revenue = Order.objects.aggregate(Sum('total_price'))

        report = {
            "total_orders": total_orders,
            "average_order_value": avg_order_value['total_price__avg'],
            "total_revenue": total_revenue['total_price__sum']
        }
        return Response(report)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Car

class CarDetailView(APIView):
    def get(self, request, car_id):
        try:
            car = Car.objects.get(id=car_id)
            data = {
                "id": car.id,
                "model": car.model,
                "manufacturer": car.manufacturer,
                "year": car.year
            }
            return Response(data, status=status.HTTP_200_OK)
        except Car.DoesNotExist:
            return Response({"error": "Car not found"}, status=status.HTTP_404_NOT_FOUND)
