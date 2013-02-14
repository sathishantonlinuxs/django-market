from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import loader
from django.template.context import RequestContext
from models import Category, Product, Image
from django.views.generic.list import ListView
from cart import Cart
from django.db.models import Count
import random
from forms import ImageForm


def getTemplateDictionary():
  categoryList = Category.objects.all();
  dictMap = {}
  dictMap['categoryList'] = categoryList
  return dictMap


def getDefaultMaps(dict):
  categoryList = Category.objects.annotate(numProduct=Count('product')).filter(numProduct__gt=0)
  dbProductList = Product.objects.all()
  defaultDict = {'categoryList': categoryList, 'dbProductList': dbProductList}
  defaultDict.update(dict)
  return defaultDict


def index(request):
  #categoryList = Category.objects.all();
  dbProductList = Product.objects.all();
  # filter out all aggregated objects that are greater 0
  categoryList = Category.objects.annotate(numProduct=Count('product')).filter(numProduct__gt=0)
  #print countMap[0].categoryName, countMap[0].count
  # random list of
  productList = random.sample(dbProductList, dbProductList.count());
  template = loader.get_template('base/main.html')
  # Using RequestContext instead of Context resolves Template Context Variables like STATIC_URL
  context = RequestContext(request, {"categoryList": categoryList, "productList": productList})
  return HttpResponse(template.render(context))


def productByCategory(request, id):
  productList = Product.objects.filter(category=id);
  template = loader.get_template('category/productByCategory.html')
  context = RequestContext(request, {"productList": productList})

  return HttpResponse(template.render(context))


def listCategories(request):
  categoryList = Category.objects.all();
  template = loader.get_template('category/categoryOverview.html')
  # Using RequestContext instead of Context resolves Template Context Variables like STATIC_URL
  context = RequestContext(request, {"categoryList": categoryList})
  return HttpResponse(template.render(context))


def getProductByCategory(request, id):
  productList = Product.objects.filter(category=id);
  categoryList = Category.objects.all();
  template = loader.get_template('category/productByCategory.html')
  dictMap = {"productList": productList}
  context = RequestContext(request, dict(dictMap.items() + getTemplateDictionary().items()))
  return HttpResponse(template.render(context))

# def addToCard(request, productId, quantity):
def addToCard(request, product_id):
  product = Product.objects.get(id=product_id)
  category = product.category.get()
  cart = Cart(request)
  cart.add(product, product.pricePerUnit, 1)
  return getProductByCategory(request, category)


def upload(request):
  # Handle file upload
  if request.method == 'POST':
    form = ImageForm(request.POST, request.FILES)
    if form.is_valid():
      image = Image(imageFile=request.FILES['imageFile'])
      image.save()

      # Redirect to the document list after POST
      return HttpResponseRedirect(reverse('shop.views.upload'))
  else:
    form = ImageForm() # A empty, unbound form

  # Load documents for the list page
  images = Image.objects.all()

  # Render list page with the documents and the form
  return render_to_response(
    'misc/uploadFile.html',
    getDefaultMaps({'images': images, 'form': form}),
    context_instance=RequestContext(request)
  )
    
    