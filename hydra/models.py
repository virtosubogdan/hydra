from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

PRIORITY = ((1, "Low"),
            (2, "Medium"),
            (3, "High"),
            (4, "Emergency"),
            )


class Ticket(models.Model):
    requester = models.ForeignKey(User)
    priority = models.IntegerField(choices=PRIORITY)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User)
    ticket = models.ForeignKey(Ticket)
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __unicode__(self):
        return "%s by %s" % (self.title, self.author)


class Attachment(models.Model):
    ticket = models.ForeignKey(Ticket)
    filename = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    mime = models.CharField(max_length=30)


admin.site.register(Ticket)
admin.site.register(Comment)
admin.site.register(Attachment)
