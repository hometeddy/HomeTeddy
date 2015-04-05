from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import smart_unicode
from service.models import ItemType
from service.models import Item

# UserProfile Model
class UserProfile(models.Model):
    # User 1to1 foreign key
    user = models.OneToOneField(User, related_name="profile")
    # User Profile extension fields
    display_name = models.CharField(max_length=200)
    # Gender
    DEFAULT = 'G'
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    GENDER_CHOICE = (
        (DEFAULT, 'Gender'),
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    )
    gender = models.CharField(max_length=2,
                              choices=GENDER_CHOICE,
                              default=DEFAULT)
    #Photo
    photo = models.CharField(max_length=200)
    introduction = models.CharField(max_length=200)
    # address fields
    address = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    # Contact
    phone = models.CharField(max_length=20)
    # foreign keys

    ItemType = models.ForeignKey(ItemType, default=1)


    # Audit
    # Created = models.DateField.auto_now_add(editable = False)
    # Updated = models.DateField.auto_now(editable = False)


    def __unicode__(self):
        return smart_unicode(self.name)


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


