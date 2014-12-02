import pickle
import base64
import datetime

from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models

from oauth2client.django_orm import FlowField
from oauth2client.django_orm import CredentialsField



class CredentialsModel(models.Model):
  id = models.ForeignKey(User, primary_key=True)
  credential = CredentialsField()
  
  
class Tweet(models.Model):
    text = models.TextField(max_length=150)
    timeDate = models.DateTimeField(auto_now=True)
    
    
    def __unicode__(self):
      return u'%s' % (self.text)
    

class HashTag(models.Model):
    tag = models.CharField(max_length=45)
    timeDate = models.DateTimeField(auto_now=True)
    tweets = models.ManyToManyField(Tweet, blank=True, null=True)
    classroomID = models.IntegerField()
    
    
    def __unicode__(self):
      return u'%s' % (self.tag)

    
class Classroom(models.Model):
    name = models.CharField(max_length=45)
    code = models.CharField(max_length=10)
    tweets = models.ManyToManyField(Tweet, blank=True, null=True)
    allowJoin = models.BooleanField()
    classOwnerID = models.IntegerField()


    def __unicode__(self):
      return u'%s' % (self.name)

class Favorite(models.Model):
    tweets = models.ForeignKey(Tweet)

class UserInfo(models.Model):
    user = models.ForeignKey(User)
    avatarColor = models.CharField(max_length=45, blank=True, null=True)
    teacher = models.BooleanField()
    mr_ms = models.CharField(max_length=45, blank=True, null=True)
    readOnly = models.BooleanField()
    tweets = models.ManyToManyField(Tweet, blank=True, null=True)
    classrooms = models.ManyToManyField(Classroom, blank=True, null=True)
    favorites = models.ManyToManyField(Favorite, blank=True, null=True)
    backColor = models.CharField(max_length=45, blank=True, null=True)
    textColor = models.CharField(max_length=45, blank=True, null=True)
    avatarBackColor = models.CharField(max_length=45, blank=True, null=True)
    avatarTextColor = models.CharField(max_length=45, blank=True, null=True)


    def __unicode__(self):
      return u'%s' % (self.user)
    











class CredentialsAdmin(admin.ModelAdmin):
    pass


admin.site.register(CredentialsModel, CredentialsAdmin)











