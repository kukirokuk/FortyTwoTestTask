from django.db import models


class SavedRequest(models.Model):
    host = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    method = models.CharField(max_length=255, blank=True)
    priority = models.IntegerField(default=1)

    def __unicode__(self):
        return "%s, %s" % (self.host, self.path)
