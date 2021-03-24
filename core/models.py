from django.db import models
from django.db.models.aggregates import Count, Avg, Max, Min

# Create your models here.


class GroupManager(models.Manager):
    
    def get_group_with_student_count(self):
        return self.get_queryset().annotate(stq=Count('student'), stavg=Avg('student__age'), stmax=Max('student__age'), stmin=Min('student__age'))


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

    objects = GroupManager()


class Student(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    age = models.PositiveSmallIntegerField()
    email = models.EmailField(max_length=50)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

