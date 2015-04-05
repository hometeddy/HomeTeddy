from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import smart_unicode
from service.models import ItemType
from service.models import Item
# Create your models here.


class Profile(models.Model):
    # user = models.OneToOneField(User)
    name = models.CharField(max_length=200)
    photo = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.IntegerField(max_length=20)
    desc = models.CharField(max_length=200)
    ItemType = models.ForeignKey(ItemType)

    def __unicode__(self):
        return smart_unicode(self.name)



class ServiceList(models.Model):
    price = models.IntegerField(max_length=20)
    profile = models.ForeignKey(Profile)
    item = models.ForeignKey(Item)

    def __unicode__(self):
        return smart_unicode(self.price)
