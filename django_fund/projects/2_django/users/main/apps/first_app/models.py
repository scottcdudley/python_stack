from __future__ import unicode_literals
from django.db import models
import re

class Users( models.Model):
    first_name = models.CharField( max_length = 255 )
    last_name = models.CharField( max_length = 255 )
    email_address = models.CharField( max_length = 255 )
    age = models.IntegerField()
    created_at = models.DateTimeField( auto_now_add = True )
    updated_at = models.DateTimeField( auto_now_add = True )

    def __repr__(self):
        return '<user:{} {} {}>' .format (self.id, self.first_name, self.last_name, self.email_address, self.age)
    