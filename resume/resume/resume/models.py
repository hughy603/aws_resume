from django.db import models
from django.core.exceptions import ValidationError



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
    degree = models.CharField(max_length=255)
    college = models.CharField(max_length=255)
    start_year = models.IntegerField()
    end_year = models.IntegerField()

    def clean(self):
        if self.start_year > 9999 or self.end_year > 9999:
            raise ValidationError('The year cannot be greater than 9999')
        if self.start_year < 1900 or self.end_year < 1900:
            raise ValidationError('The year cannot be less than 1900')
        if self.start_year > self.end_year:
            raise ValidationError('The start year must be less than or equal to the end year')

    def __str__(self):
        return self.degree

class Person(DateMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12, blank=True)
    linked_in = models.CharField(max_length=255, blank=True)
    github = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255)
    education = models.ManyToManyField(Education, null=True)

    def __str__(self):
        return "{self.first_name} {self.last_name}".format(self=self)



class Resume(DateMixin):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    skills = models.ManyToManyField(Skill)
