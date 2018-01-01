from django.db import models
from members.models import Member


class Topic(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    topic = models.ForeignKey(Topic, null=True, blank=True)
    author = models.ForeignKey(Member, null=True, blank=True)
    date = models.DateTimeField("date published", null=True, blank=True)
    lastUpdated = models.DateTimeField("last updated", null=True, blank=True)
    
    def __unicode__(self):
        return self.title + "  by  " + self.author.user.username

    def __str__(self):
        return self.title + "  by  " + self.author.user.username

class Reply(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(Member, null=True, blank=True)
    post = models.ForeignKey(Post, null=True, blank=True)
    date = models.DateTimeField("date published", null=True, blank=True)

    def __unicode__(self):
        return self.title + "  by  " + self.author.user.username + "  to  [" + self.post.title + "  by  " + self.post.author.user.username+"]"

    def __str__(self):
        return self.title + "  by  " + self.author.user.username + "  to  [" + self.post.title + "  by  " + self.post.author.user.username+"]"
