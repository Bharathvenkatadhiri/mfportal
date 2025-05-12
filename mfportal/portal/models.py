from django.db import models

class Partmaster(models.Model):
    id = models.AutoField(primary_key=True)
    created_by = models.CharField(max_length=50, null=True, blank=True)
    createdDate = models.DateTimeField(auto_now_add=True) 
    LastModifiedDate = models.DateTimeField(auto_now=True)
    CurrencyIsoCode = models.CharField(max_length=50, null=True, blank=True)
    Density_g_cc = models.DecimalField(max_digits=12, decimal_places=4, null=True, blank=True)
    Diameter_mm =models.DecimalField(max_digits=16, decimal_places=2, null=True, blank=True)
    Length_mm = models.DecimalField(max_digits=16, decimal_places=2, null=True, blank=True)
    part_master_name = models.CharField(max_length=80, null=True, blank=True)
    part_name = models.CharField(max_length=255, null=True, blank=True)
    part_number = models.CharField(max_length=255, null=True, blank=True)
    raw_material = models.CharField(max_length=50, null=True, blank=True)
    shape = models.CharField(max_length=50, null=True, blank=True)
    thickness_mm = models.DecimalField(max_digits=16, decimal_places=2, null=True, blank=True)
    weight_of_the_part_grams = models.DecimalField(max_digits=16, decimal_places=2, null=True, blank=True)
    weight_of_the_part_kg = models.DecimalField(max_digits=16, decimal_places=2, null=True, blank=True)
    width_mm = models.DecimalField(max_digits=16, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.id
    
class Purchaseorder(models.Model):
    id = models.AutoField(primary_key=True)
    created_by = models.CharField(max_length=50, null=True, blank=True)
    createdDate = models.DateTimeField(auto_now_add=True) 
    LastModifiedDate = models.DateTimeField(auto_now=True)
    CurrencyIsoCode = models.CharField(max_length=50, null=True, blank=True)
    Asset_Expenses = models.DecimalField(max_digits=16, decimal_places=2, null=True, blank=True)
    Comments = models.CharField(max_length=255, null=True, blank=True)
    Delivery_due_date = models.DateField(null=True, blank=True)
    Detailed_comments = models.TextField(null=True, blank=True)
    Fulfilled_Amount = models.DecimalField(max_digits=16, decimal_places=2, null=True, blank=True)
    purchase_order_name = models.CharField(max_length=80, null=True, blank=True)
    overall_expenses = models.DecimalField(max_digits=16, decimal_places=2, null=True, blank=True)
    project_status = models.CharField(max_length=255, null=True, blank=True)
    purchase_order_details = models.CharField(max_length=255, null=True, blank=True)
    purchase_order_value = models.DecimalField(max_digits=16, decimal_places=2, null=True, blank=True)
    vendor_expenses = models.DecimalField(max_digits=16, decimal_places=2, null=True, blank=True)

class Part(models.Model):
    id = models.AutoField(primary_key=True)
    created_by = models.CharField(max_length=50, null=True, blank=True)
    createdDate = models.DateTimeField(auto_now_add=True) 
    LastModifiedDate = models.DateTimeField(auto_now=True)
    CurrencyIsoCode = models.CharField(max_length=50, null=True, blank=True)
    Fulfilled_Amount = models.DecimalField(max_digits=16, decimal_places=2, null=True, blank=True)
    Fulfilled_Quantity = models.DecimalField(max_digits=18, decimal_places=0, null=True, blank=True)
    Machining_Type = models.TextField(null=True, blank=True)
    part_master = models.ForeignKey(
        'Partmaster',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='parts'
    )
    part_name = models.CharField(max_length=255, null=True, blank=True)
    part_number = models.CharField(max_length=255, null=True, blank=True)
    Part_Number_auto = models.TextField(null=True, blank=True)
    purchase_order = models.ForeignKey(
        'Purchaseorder',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='purchase'
    )
    Quantity = models.DecimalField(max_digits=18, decimal_places=0, null=True, blank=True)
    Total_Price = models.DecimalField(max_digits=16, decimal_places=2, null=True, blank=True)
    Total_raw_Material_Weight_to_be_ordered_kg = models.DecimalField(max_digits=16, decimal_places=2, null=True, blank=True)
    unit_price = models.DecimalField(max_digits=16, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.id
    
class Vendormaster(models.Model):
    id = models.AutoField(primary_key=True)
    created_by = models.CharField(max_length=50, null=True, blank=True)
    createdDate = models.DateTimeField(auto_now_add=True) 
    LastModifiedDate = models.DateTimeField(auto_now=True)
    CurrencyIsoCode = models.CharField(max_length=50, null=True, blank=True)
    vendor_master_name = models.CharField(max_length=80, null=True, blank=True)
    vendor_name = models.CharField(max_length=255, null=True, blank=True)
    part_number = models.CharField(max_length=255, null=True, blank=True)
    Address = models.TextField(null=True, blank=True)
    GST_number = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.id
    
class Vendorinvoice(models.Model):
    id = models.AutoField(primary_key=True)
    created_by = models.CharField(max_length=50, null=True, blank=True)
    createdDate = models.DateTimeField(auto_now_add=True) 
    LastModifiedDate = models.DateTimeField(auto_now=True)
    CurrencyIsoCode = models.CharField(max_length=50, null=True, blank=True)
    Comments = models.CharField(max_length=255, null=True, blank=True)    
    Due_date = models.DateField(null=True, blank=True)
    Invoice_date = models.DateField(null=True, blank=True)
    Invoice_url = models.CharField(max_length=255, null=True, blank=True)
    vendor_invoice_number = models.CharField(max_length=80, null=True, blank=True)
    Paid_amount = models.DecimalField(max_digits=16, decimal_places=2, null=True, blank=True)
    Paid_date = models.DateField(null=True, blank=True)
    Total = models.DecimalField(max_digits=16, decimal_places=2, null=True, blank=True)
    vendor_master = models.ForeignKey(
        'Vendormaster',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='vendor'
    )

    def __str__(self):
        return self.id
    
class Vendorinvoicetransaction(models.Model):
    id = models.AutoField(primary_key=True)
    created_by = models.CharField(max_length=50, null=True, blank=True)
    createdDate = models.DateTimeField(auto_now_add=True) 
    LastModifiedDate = models.DateTimeField(auto_now=True)
    CurrencyIsoCode = models.CharField(max_length=50, null=True, blank=True)
    Amount = models.DecimalField(max_digits=16, decimal_places=2, null=True, blank=True)    
    cube_part_number = models.TextField(null=True, blank=True)
    Description = models.CharField(max_length=255, null=True, blank=True)
    GST_amount = models.DecimalField(max_digits=16, decimal_places=2, null=True, blank=True)
    GST_per = models.DecimalField(max_digits=18, decimal_places=0, null=True, blank=True)
    Invoice_type = models.CharField(max_length=255, null=True, blank=True)
    is_asset = models.BooleanField(default=False)
    vendor_invoice_transaction_name = models.CharField(max_length=80, null=True, blank=True)
    Non_prouction_hours = models.DecimalField(max_digits=18, decimal_places=0, null=True, blank=True)
    Other_charges = models.DecimalField(max_digits=16, decimal_places=2, null=True, blank=True)
    Paid = models.BooleanField(default=True)
    Paid_by = models.CharField(max_length=255, null=True, blank=True)
    part = models.ForeignKey(
        'Part',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='part'
    )
    Price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    Production_hours_today = models.DecimalField(max_digits=16, decimal_places=2, null=True, blank=True)
    purchase_order = models.ForeignKey(
        'Purchaseorder',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='purchase_order'
    )
    Total = models.DecimalField(max_digits=16, decimal_places=2, null=True, blank=True)
    Transaction_date = models.DateField(null=True, blank=True)
    vendor_invoice = models.ForeignKey(
        'Vendorinvoice',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='vendorinvoice'
    )
    Weight_quantity = models.DecimalField(max_digits=16, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.id