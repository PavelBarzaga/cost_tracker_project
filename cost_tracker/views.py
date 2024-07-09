from rest_framework import generics
from .models import Cost
from .serializers import CostSerializer
from rest_framework import filters


class CostListCreateView(generics.ListCreateAPIView):
    queryset = Cost.objects.all()
    serializer_class = CostSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["category", "amount", "date"]
    ordering_fields = ["category", "amount", "date"]


class CostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cost.objects.all()
    serializer_class = CostSerializer
