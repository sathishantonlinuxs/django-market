from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.db.models import Count


class Address(models.Model):
  surName = models.CharField(max_length=150)
  firstName = models.CharField(max_length=50)
  streetName = models.CharField(max_length=100)
  zipCode = models.IntegerField()
  city = models.CharField(max_length=50)
  country = models.CharField(max_length=50)
  email = models.EmailField();


class Label(models.Model):
  labelName = models.CharField(max_length=25)

class Division(models.Model):
  divisionName = models.CharField(max_length=50)

  def __unicode__(self):
    return self.divisionName


class Producer(models.Model):
  address = models.ForeignKey(Address)
  shortName = models.CharField(max_length=70)
  def __unicode__(self):
    return self.shortName

class Category(models.Model):
  categoryName = models.CharField(max_length=50)
  def __unicode__(self):
    return self.categoryName

class Product(models.Model):
  producer = models.ForeignKey(Producer)
  headline = models.CharField(max_length=200)
  description = models.TextField()
  publishDate = models.DateTimeField('Date published')
  quantityUnit = models.CharField(max_length=20)
  endurance = models.DecimalField(max_digits=5, decimal_places=1)
  active = models.BooleanField()
  label = models.ManyToManyField(Label, null=True, blank=True)
  category = models.ManyToManyField(Category)
  division = models.ForeignKey(Division, null=True)
  pricePerUnit = models.DecimalField(max_digits=5, decimal_places=2);


  def __unicode__(self):
    return self.headline



class Image(models.Model):
  path = models.CharField(max_length=200)
  product = models.ForeignKey(Product)

# The login class enhancing the user from the auth module
class UserProfile(models.Model):
  user = models.OneToOneField(User)
  address = models.ForeignKey(Address)

class Document(models.Model):
  docfile = models.FileField(upload_to='files')

def create_user_profile(sender, instance, created, **kwargs):
  if created:
    UserProfile.objects.create(user=instance)



post_save.connect(create_user_profile, sender=User)


