from django.contrib import admin

from . import models

admin.site.register(models.Person)
admin.site.register(models.Skill)
admin.site.register(models.Resume)
admin.site.register(models.Education)
