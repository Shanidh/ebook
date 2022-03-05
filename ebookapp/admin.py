from django.contrib import admin
from .import models
# Register your models here.

admin.site.register(models.Ebook)
admin.site.register(models.User)
admin.site.register(models.Usertoken)
