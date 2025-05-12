from django.urls import path
from .views import (
    PartmasterListCreateView, PartmasterDetailView,
    PurchaseorderListCreateView, PurchaseorderDetailView,
    PartListCreateView, PartDetailView,
    VendormasterListCreateView, VendormasterDetailView,
    VendorinvoiceListCreateView, VendorinvoiceDetailView,
    VendorinvoicetransationListCreateView, VendorinvoicetransationDetailView
)

urlpatterns = [
    path('partmaster/', PartmasterListCreateView.as_view(), name='partmaster-list-create'),
    path('partmaster/<int:pk>/', PartmasterDetailView.as_view(), name='partmaster-detail'),
    path('purchaseorder/', PurchaseorderListCreateView.as_view(), name='purchaseorder-list-create'),
    path('purchaseorder/<int:pk>/', PurchaseorderDetailView.as_view(), name='purchaseorder-detail'),
    path('part/', PartListCreateView.as_view(), name='part-list-create'),
    path('part/<int:pk>/', PartDetailView.as_view(), name='part-detail'),
    path('vendormaster/', VendormasterListCreateView.as_view(), name='vendormaster-list-create'),
    path('vendormaster/<int:pk>/', VendormasterDetailView.as_view(), name='vendormaster-detail'),
    path('vendorinvoice/', VendorinvoiceListCreateView.as_view(), name='vendorinvoice-list-create'),
    path('vendorinvoice/<int:pk>/', VendorinvoiceDetailView.as_view(), name='vendorinvoice-detail'),
    path('vendorinvoicetransaction/', VendorinvoicetransationListCreateView.as_view(), name='vendorinvoicetransaction-list-create'),
    path('vendorinvoicetransaction/<int:pk>/', VendorinvoicetransationDetailView.as_view(), name='vendorinvoicetransaction-detail'),                    
]