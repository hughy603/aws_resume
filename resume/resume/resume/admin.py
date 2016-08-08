from django.contrib import admin

from .models import (
    Person,
    Skill,
    Resume,
)


admin.site.register(Person)
admin.site.register(Skill)
admin.site.register(Resume)
