from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from task.forms import TaskCreatingForm
from task.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskCreatingForm
    success_url = reverse_lazy("task:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("task:task-list")


class TaskDeleteView( generic.DeleteView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("task:task-list")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("task:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("task:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("task:tag-list")


def complete_task(request, pk):
    task = Task.objects.get(id=pk)
    if task.done:
        task.done = False
    else:
        task.done = True
    task.save()
    return HttpResponseRedirect(reverse_lazy("task:task-list"))
