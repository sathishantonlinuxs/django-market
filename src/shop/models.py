from django.db import models


    
class Address(models.Model):
    surName = models.CharField(max_length=150)
    firstName = models.CharField(max_length=50)
    streetName = models.CharField(max_length=100)
    zipCode = models.IntegerField()
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    email = models.EmailField();
    
    
class Label(models.Model):
    labelName = models.CharField(max_length=25);
    
class Category(models.Model):
    categoryName = models.CharField(max_length=25);
    
class Producer(models.Model):
    address = models.ForeignKey(Address)
    shortName = models.CharField(max_length=70)
    
class Product(models.Model):
    headline = models.CharField(max_length=200)
    description = models.TextField()
    publishDate = models.DateTimeField('Date published')
    producer = models.ForeignKey(Producer)
    # something like pc, volume,
    quantityUnit = models.CharField(max_length=20)
    # period in days
    endurance = models.DecimalField(max_digits=5, decimal_places=1)
    active = models.BooleanField()
    label = models.ManyToManyField(Label)
    category = models.ManyToManyField(Category)
    
class Image(models.Model):
    path = models.CharField(max_length=200);
    product = models.ForeignKey(Product)
    

    
    
    
    

    

    

    
    
