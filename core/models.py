from django.db import models

# Create your models here.


class Teacher(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    email = models.EmailField(max_length=50)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    teachers = models.ManyToManyField(Teacher)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    email = models.EmailField(max_length=50)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

