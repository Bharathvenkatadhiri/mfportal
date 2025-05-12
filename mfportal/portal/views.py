from rest_framework import generics
from .models import Partmaster, Purchaseorder, Part, Vendormaster, Vendorinvoice, Vendorinvoicetransaction
from .serializers import PartmasterSerializer, PurchaseorderSerializer, PartSerializer, \
    VendormasterSerializer, VendorinvoiceSerializer, VendorinvoicetransactionSerializer

class PartmasterListCreateView(generics.ListCreateAPIView):
    queryset = Partmaster.objects.all()
    serializer_class = PartmasterSerializer

class PartmasterDetailView(generics.RetrieveUpdateAPIView):
    queryset = Partmaster.objects.all()
    serializer_class = PartmasterSerializer

class PurchaseorderListCreateView(generics.ListCreateAPIView):
    queryset = Purchaseorder.objects.all()
    serializer_class = PurchaseorderSerializer

class PurchaseorderDetailView(generics.RetrieveUpdateAPIView):
    queryset = Purchaseorder.objects.all()
    serializer_class = PurchaseorderSerializer

class PartListCreateView(generics.ListCreateAPIView):
    queryset = Part.objects.all()
    serializer_class = PartSerializer

class PartDetailView(generics.RetrieveUpdateAPIView):
    queryset = Part.objects.all()
    serializer_class = PartSerializer

class VendormasterListCreateView(generics.ListCreateAPIView):
    queryset = Vendormaster.objects.all()
    serializer_class = VendormasterSerializer

class VendormasterDetailView(generics.RetrieveUpdateAPIView):
    queryset = Vendormaster.objects.all()
    serializer_class = VendormasterSerializer

class VendorinvoiceListCreateView(generics.ListCreateAPIView):
    queryset = Vendorinvoice.objects.all()
    serializer_class = VendorinvoiceSerializer

class VendorinvoiceDetailView(generics.RetrieveUpdateAPIView):
    queryset = Vendorinvoice.objects.all()
    serializer_class = VendorinvoiceSerializer

class VendorinvoicetransationListCreateView(generics.ListCreateAPIView):
    queryset = Vendorinvoicetransaction.objects.all()
    serializer_class = VendorinvoicetransactionSerializer

class VendorinvoicetransationDetailView(generics.RetrieveUpdateAPIView):
    queryset = Vendorinvoicetransaction.objects.all()
    serializer_class = VendorinvoicetransactionSerializer