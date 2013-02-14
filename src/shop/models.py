from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.db.models import Count
from django.conf import settings
from PIL import Image
from cStringIO import StringIO
from django.core.files.uploadedfile import SimpleUploadedFile
import os


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


class Image(models.Model):

  imageFile = models.ImageField(upload_to='files')
  imageCaption = models.CharField(max_length=255, blank=True, null=True)
  imageThumbnailFile = models.ImageField(upload_to='files', max_length=500, blank=True, null=True)
  imageThumbnailSquaredFile = models.ImageField(upload_to='files', max_length=500, blank=True, null=True)

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
    if not self.image:
      return

    DJANGO_TYPE = self.imageFile.file.content_type

    if DJANGO_TYPE == 'image/jpeg':
      PIL_TYPE = 'jpeg'
      FILE_EXTENSION = 'jpg'
    elif DJANGO_TYPE == 'image/png':
      PIL_TYPE = 'png'
      FILE_EXTENSION = 'png'

    # Open original photo which we want to thumbnail using PIL's Image
    image = Image.open(StringIO(self.imageFile.read()))
    # can be done: image = image.convert('RGB')
    assert isinstance(image.thumbnail, Image)
    # max height, max width
    image.thumbnail((200,200), Image.ANTIALIAS)

    # Save the thumbnail
    temp_handle = StringIO()
    image.save(temp_handle, PIL_TYPE)
    temp_handle.seek(0)

    # Save image to a SimpleUploadedFile which can be saved into
    # ImageField
    suf = SimpleUploadedFile(os.path.split(self.image.name)[-1],
      temp_handle.read(), content_type=DJANGO_TYPE)
    # Save SimpleUploadedFile into image field
    self.imageThumbnailFile.save('%s_thumbnail.%s' % (os.path.splitext(suf.name)[0], FILE_EXTENSION), suf, save=False)

  def save(self):
    # save the original first
    super(Image, self).save()
    # create and save the thumbnail
    self.create_thumbnail()

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




