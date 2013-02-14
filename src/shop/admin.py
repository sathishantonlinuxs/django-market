from django.contrib import admin
from models import Product, Producer, UserProfile, Address, Category, Division, Image



class ImagesAdmin(admin.ModelAdmin):
  list_display = ('image_img',)


admin.site.register(Product)
admin.site.register(Producer)
admin.site.register(UserProfile)
admin.site.register(Address)
admin.site.register(Category)
admin.site.register(Division)
admin.site.register(Image, ImagesAdmin)






