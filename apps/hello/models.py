from django.db import models


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

    def __unicode__(self):
        return 'Contact: %s' % self.name
