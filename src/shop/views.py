from django.http import HttpResponse
from django.template import loader
from django.template.context import RequestContext
from shop.models import Category, Product
from django.views.generic.list import ListView
from cart import Cart

def getTemplateDictionary():
    categoryList = Category.objects.all();
    dictMap = {}
    dictMap['categoryList'] = categoryList

    return dictMap

def index(request):
    categoryList = Category.objects.all();
    template = loader.get_template('category/categoryOverview.html')
    # Using RequestContext instead of Context resolves Template Context Variables like STATIC_URL
    context = RequestContext(request, {"categoryList" : categoryList })
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

def addToCard(request, productId, quantity):
    product = Product.objects.get(id=productId)
    cart = Cart(request)
    cart.add(product, product.unit_price, quantity)
    
    