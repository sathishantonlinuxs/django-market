from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


urlpatterns = patterns('',
  # Examples:
  # url(r'^$', 'DjangoMarket.views.home', name='home'),
  # url(r'^DjangoMarket/', include('DjangoMarket.foo.urls')),

  # Uncomment the admin/doc line below to enable admin documentation:
  # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

  # Uncomment the next line to enable the admin:
  url(r'^$', 'shop.views.index'),
  url(r'^category/(?P<id>\d+)/$', 'shop.views.getProductByCategory'),
  url(r'^product/(?P<product_id>\d+)/toBasket/$', 'shop.views.addToCard'),
  #url(r'^category/(?<poll_id>\d+)/$', 'detail'),
)

urlpatterns += staticfiles_urlpatterns()
