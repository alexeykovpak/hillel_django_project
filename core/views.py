from django.shortcuts import render
from django.views.generic.list import ListView
from core.models import Group, Teacher

# Create your views here.

class GroupView(ListView):
    template_name = 'group_index.html'
    model = Group

    def get_context_data(self, **kwargs):
        context = super(GroupView, self).get_context_data(**kwargs)
        groups = Group.objects.get_group_with_student_count().prefetch_related('teachers')
        context['groups'] = groups
        return context


class TeacherView(ListView):
    template_name = 'teacher_index.html'
    model = Teacher


