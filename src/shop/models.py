from cStringIO import StringIO
import os

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
from ImageConversion import Converter


class Address(models.Model):
  surName = models.CharField(max_length=150)
  firstName = models.CharField(max_length=50)
  streetName = models.CharField(max_length=100)
  zipCode = models.IntegerField()
  city = models.CharField(max_length=50)
  country = models.CharField(max_length=50)
  email = models.EmailField()


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


class Image(models.Model):
  imageFile = models.ImageField(upload_to='files')
  imageCaption = models.CharField(max_length=255, blank=True, null=True)
  imageThumbnailFile = models.ImageField(upload_to='files', max_length=500, blank=True, null=True)
  imageThumbnailSquaredFile = models.ImageField(upload_to='files', max_length=500, blank=True, null=True)
  imageThumbnailBWFile = models.ImageField(upload_to='files', max_length=500, blank=True, null=True)

  def image_img(self):
    if self.imageFile:
      return u'<img src="%s" />' % self.imageFile.url
    else:
      return '(Sin imagen)'

  image_img.short_description = 'Thumb'
  image_img.allow_tags = True

  def __unicode__(self):
    return self.imageFile.path

  def create_thumbnail(self):
    # Original code: http://snipt.net/danfreak/generate-thumbnails-in-django-with-pil/
    # And http://www.yilmazhuseyin.com/blog/dev/create-thumbnails-imagefield-django/

    converter = Converter(self.imageFile)
    image = converter.reduceSize()

    # Save the thumbnail
    temp_handle = StringIO()
    image.save(temp_handle, converter.PIL_TYPE)
    temp_handle.seek(0)
    suf = SimpleUploadedFile(os.path.split(self.imageFile.name)[-1],
                             temp_handle.read(), content_type=converter.DJANGO_TYPE)
    # Save SimpleUploadedFile into image field
    self.imageThumbnailFile.save('%s_thumbnail.%s' % (os.path.splitext(suf.name)[0], converter.FILE_EXTENSION), suf, save=False)

    temp_handle = StringIO()
    squaredImage = converter.createCenteredSquare()
    squaredImage.save(temp_handle, converter.PIL_TYPE)
    temp_handle.seek(0)
    suf = SimpleUploadedFile(os.path.split(self.imageFile.name)[-1],
                             temp_handle.read(), content_type=converter.DJANGO_TYPE)
    self.imageThumbnailSquaredFile.save('%s_thumbnail_squared.%s' % (os.path.splitext(suf.name)[0], converter.FILE_EXTENSION), suf, save=False)

    bwImage = squaredImage.convert("L")
    temp_handle = StringIO()

    bwImage.save(temp_handle, converter.PIL_TYPE)
    temp_handle.seek(0)
    suf = SimpleUploadedFile(os.path.split(self.imageFile.name)[-1],
                             temp_handle.read(), content_type=converter.DJANGO_TYPE)
    self.imageThumbnailBWFile.save('%s_thumbnail_bw.%s' % (os.path.splitext(suf.name)[0], converter.FILE_EXTENSION), suf, save=False)


  def save(self):
    print "Invoked save on image"
    self.create_thumbnail()
    super(Image, self).save()


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
  pricePerUnit = models.DecimalField(max_digits=5, decimal_places=2)
  productImage = models.ForeignKey(Image, null=True)


  def __unicode__(self):
    return self.headline

# The login class enhancing the user from the auth module
class UserProfile(models.Model):
  user = models.OneToOneField(User)
  address = models.ForeignKey(Address)


def create_user_profile(sender, instance, created, **kwargs):
  if created:
    UserProfile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User)




