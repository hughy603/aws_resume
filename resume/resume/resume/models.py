from django.db import models


class DateMixin(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Person(DateMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return "{self.first_name} {self.last_name}".format(self=self)
