from django import forms
from django.forms import DateTimeField

from task.models import Task


class TaskCreatingForm(forms.ModelForm):
    deadline = DateTimeField(input_formats=['%Y-%m-%d %H:%M'])

    class Meta:
        model = Task
        fields = "__all__"
