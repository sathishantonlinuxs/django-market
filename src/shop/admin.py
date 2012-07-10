from django.contrib import admin
from shop.models import Product, Producer, UserProfile, Address, Category

admin.site.register(Product)
admin.site.register(Producer)
admin.site.register(UserProfile)
admin.site.register(Address)
admin.site.register(Category)
