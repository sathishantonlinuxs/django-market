from django.http import HttpResponse
from django.template import loader
from django.template.context import RequestContext
from shop.models import Category

def index(request):
    categoryList = Category.objects.all();
    template = loader.get_template('category/categoryTree.html')
    # Using RequestContext instead of Context resolves Template Context Variables like STATIC_URL
    context = RequestContext(request, {"categoryList" : categoryList })
    return HttpResponse(template.render(context))

#def category(request):
