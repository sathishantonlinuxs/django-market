from PIL import Image
import PIL
from cStringIO import StringIO

__author__ = 'Heiko Kundlacz'


class Converter(object):
  def __init__(self, imageFile):
    self.imageFile = imageFile

    self.DJANGO_TYPE = self.imageFile.file.content_type
    if self.DJANGO_TYPE == 'image/jpeg':
      self.PIL_TYPE = 'jpeg'
      self.FILE_EXTENSION = 'jpg'
    elif self.DJANGO_TYPE == 'image/png':
      self.PIL_TYPE = 'png'
      self.FILE_EXTENSION = 'png'
    self.image = Image.open(StringIO(self.imageFile.read()))


  def reduceSize(self, baseSize=(250, 250)):
    reducedImage = self.image.copy()
    reducedImage.thumbnail(baseSize, Image.ANTIALIAS)
    return reducedImage

  def createCenteredSquare(self, size=250):

    width = self.image.size[0]
    height = self.image.size[1]
    widthOffset = abs(width - size) / 2
    heightOffset = abs(height - size) / 2

    tempImage = self.image.crop((widthOffset, heightOffset, widthOffset + size, heightOffset + size))
    return tempImage

