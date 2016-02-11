from django.db import models
from django_resized import ResizedImageField


# Person contacts model
class Contact(models.Model):
    name = models.CharField(max_length=40, blank=False)
    last_name = models.CharField(max_length=40, blank=False)
    date_of_birth = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    jabber = models.CharField(max_length=40)
    skype = models.CharField(max_length=40)
    other_contacts = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photo/', blank=True, null=True)
    image = ResizedImageField(size=[200, 200], upload_to='photo/', blank=True,
                              null=True)

    def __unicode__(self):
        return 'Contact: %s' % self.name


# Models edit page log model
class ModelsLog(models.Model):
    model_name = models.CharField(max_length=40, blank=True)
    action = models.CharField(max_length=40, blank=True)
    date = models.DateTimeField()

    def __unicode__(self):
        return 'model: %s %s' % (self.model_name, self.action)
