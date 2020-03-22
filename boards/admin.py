from django.contrib import admin

# Register your models here.
from boards import models
admin.site.register(models.Articles)
admin.site.register(models.Events)
admin.site.register(models.News)