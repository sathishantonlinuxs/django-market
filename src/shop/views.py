from django.http import HttpResponse
from django.template import loader
from django.template.context import RequestContext
from models import Category, Product
from django.views.generic.list import ListView
from cart import Cart
import random

def getTemplateDictionary():
    categoryList = Category.objects.all();
    dictMap = {}
    dictMap['categoryList'] = categoryList
    return dictMap

def index(request):
    categoryList = Category.objects.all();
    dbProductList = Product.objects.all();
    # random list of
    productList = random.sample(dbProductList, dbProductList.count());
    template = loader.get_template('base/main.html')
    # Using RequestContext instead of Context resolves Template Context Variables like STATIC_URL
    context = RequestContext(request, {"categoryList" : categoryList,"productList" : productList })
    return HttpResponse(template.render(context))

def productByCategory(request, id):
    productList = Product.objects.filter(category = id);
    template = loader.get_template('category/productByCategory.html')
    context = RequestContext(request, {"productList" : productList })
    
    return HttpResponse(template.render(context))

def listCategories(request):
    categoryList = Category.objects.all();
    template = loader.get_template('category/categoryOverview.html')
    
    # Using RequestContext instead of Context resolves Template Context Variables like STATIC_URL
    context = RequestContext(request, {"categoryList" : categoryList })
    return HttpResponse(template.render(context))

def getProductByCategory(request, id):
    productList = Product.objects.filter(category = id);
    categoryList = Category.objects.all();
    template = loader.get_template('category/productByCategory.html')
    dictMap = {"productList" : productList}
    context = RequestContext(request, dict(dictMap.items() + getTemplateDictionary().items()))
    return HttpResponse(template.render(context))

# def addToCard(request, productId, quantity):
def addToCard(request, product_id):
    product = Product.objects.get(id = product_id)
    category = product.category.get()
    cart = Cart(request)
    cart.add(product, product.pricePerUnit, 1)
    return getProductByCategory(request, category)


    
    