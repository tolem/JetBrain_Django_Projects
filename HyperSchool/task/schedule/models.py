from django.db import models
from django.shortcuts import reverse


# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    about = models.TextField()

    def get_absolute_url(self):
        return reverse('tutor', args=(self.pk,))

    def __str__(self):
        return self.name + " " + self.surname


class Course(models.Model):
    title = models.CharField(max_length=50)
    info = models.TextField(max_length=255)
    duration_months = models.IntegerField()
    price = models.IntegerField()
    teacher = models.ManyToManyField(Teacher)

    def get_absolute_url(self):
        return reverse('details', kwargs={'id':self.id, 'title':self.title, 'info':self.info})

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    course = models.ManyToManyField(Course)

    def __str__(self):
        return self.name + " " + self.surname
