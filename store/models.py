from django.db import models
# Create your models here.
class Promotation(models.Model):
    description=models.CharField(max_length=255);
    discount=models.FloatField();
class Collection(models.Model):
    title=models.CharField(max_length=255);
    featured_product=models.ForeignKey('Product',on_delete=models.SET_NULL,null=True,related_name='+')
class Product(models.Model):
    title=models.CharField(max_length=255);
    description=models.TextField();
    price=models.DecimalField(max_digits=6,decimal_places=2);
    inventory=models.IntegerField()
    last_updated=models.DateTimeField(auto_now=True)
    collection=models.ForeignKey(Collection,on_delete=models.PROTECT)
    promotation=models.ManyToManyField(Promotation)
class Orders(models.Model):
    PENDING='P';
    COMPLETE='C';
    FAILED='F';
    PAYMENT_STATUS_CHOICE=[(PENDING,'Pending'),(COMPLETE,'Complete'),(FAILED,'Failed'),]
    placed_at=models.DateTimeField(auto_now_add=True);
    payment_status=models.CharField(max_length=1,choices=PAYMENT_STATUS_CHOICE,default=PENDING);
    customer=models.ForeignKey('Customer',on_delete=models.PROTECT)

class Customer(models.Model):
    MEMBERSHIP_SILVER='S';
    MEMBERSHIP_BRONZE='B';
    MEMBERSHIP_GOLD='G';
    MEMBERSHIP_CHOICES=[
        (MEMBERSHIP_SILVER,'Silver'),
        (MEMBERSHIP_GOLD,'Gold'),
        (MEMBERSHIP_BRONZE,'Bronze'),];
    first_name=models.CharField(max_length=255);
    last_name=models.CharField(max_length=255);
    email=models.EmailField(unique=True);
    phone=models.CharField(max_length=255);
    birth_date=models.DateField(null=True);
    membership=models.CharField(max_length=1,choices=MEMBERSHIP_CHOICES,default=MEMBERSHIP_BRONZE);
    
class Address(models.Model):
    street=models.CharField(max_length=255);
    city=models.CharField(max_length=255);
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
class OrderItem(models.Model):
    orders=models.ForeignKey(Orders,on_delete=models.PROTECT);
    product=models.ForeignKey(Product,on_delete=models.PROTECT);
    quantity=models.PositiveSmallIntegerField();
    unit_price=models.DecimalField(max_digits=6,decimal_places=2);
class Cart(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE);
    product=models.ForeignKey(Product,on_delete=models.CASCADE);
    quantity=models.PositiveSmallIntegerField();
