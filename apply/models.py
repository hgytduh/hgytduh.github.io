from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Application(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    ign = models.CharField(max_length=100)
    position = models.CharField(max_length=20)
    details = models.TextField(max_length=600)
    status = models.ForeignKey(Status, blank=True, null = True)

    def __unicode__(self):
        return self.position + "  -  " + self.name

    def __str__(self):
        return self.position + "  -  " + self.name
