from django.shortcuts import render
from django.views.generic.list import ListView
from core.models import Group, Teacher

# Create your views here.

class GroupView(ListView):
    template_name = 'group_index.html'
    model = Group


class TeacherView(ListView):
    template_name = 'teacher_index.html'
    model = Teacher


