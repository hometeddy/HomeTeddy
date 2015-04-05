from django.contrib import admin
from service.models import Item
from service.models import ItemType

# Register your models here.

admin.site.register(Item)
admin.site.register(ItemType)

