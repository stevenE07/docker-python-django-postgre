from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Loggeable(User): 
    first_name = None
    last_name = None
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email
    