from rest_framework import serializers
from .models import Partmaster, Purchaseorder, Part, Vendormaster, Vendorinvoice, Vendorinvoicetransaction

class PartmasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partmaster
        fields = '__all__'

class PurchaseorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchaseorder
        fields = '__all__'

class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = '__all__'

class VendormasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendormaster
        fields = '__all__'

class VendorinvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendorinvoice
        fields = '__all__'

class VendorinvoicetransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendorinvoicetransaction
        fields = '__all__'                                                