from django.db import models
from django.utils.encoding import smart_unicode
# Create your models here.


class ItemType(models.Model):
    name= models.CharField(max_length=120)
    description = models.CharField(max_length=300)

    def __unicode__(self):
        return smart_unicode(self.description)


class Item(models.Model):
    item_code= models.CharField(max_length=120)
    item_description = models.CharField(max_length=300)
    ItemType = models.ForeignKey(ItemType)

    def __unicode__(self):
        return smart_unicode(self.item_description)

