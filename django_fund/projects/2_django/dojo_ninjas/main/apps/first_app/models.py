# Inside models.py
from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.TextField(max_length=255)
    state = models.TextField(max_length=255)
    desc = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<User object: {} {} {} {}>".format(self.id, self.name, self.city, self.state)
class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)   
    dojos = models.ForeignKey(Dojo, related_name = "goes_to")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<User object: {} {} {}>".format(self.id, self.first_name, self.last_name)