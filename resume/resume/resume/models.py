from django.db import models


class DateMixin(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Skill(DateMixin):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Education(DateMixin):
    pass

class Person(DateMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12, blank=True)
    linked_in = models.CharField(max_length=255, blank=True)
    github = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255)

    def __str__(self):
        return "{self.first_name} {self.last_name}".format(self=self)



class Resume(DateMixin):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    skills = models.ManyToManyField(Skill)
