from django.contrib import admin

# Register your models here.
from .models import Loggeable

admin.site.register(Loggeable)