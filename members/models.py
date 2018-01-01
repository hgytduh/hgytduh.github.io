from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    user = models.OneToOneField(User)
    title = models.CharField(max_length=100, blank=True)
    ign = models.CharField(max_length=100)

    def __unicode__(self):
    	return "["+self.title+"] "+self.user.username
    def __str__(self):
    	return "["+self.title+"] "+self.user.username