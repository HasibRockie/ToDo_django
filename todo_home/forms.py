from django import forms
from .models import ToDoModels

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDoModels
        fields = ('taskTitle', 'taskDescription')

        labels = {
            'taskTitle': 'Task Title',
            'taskDescription': 'Task Description',
            'is_completed': 'Is Completed',
        }

        placeholders = {
            'taskTitle': 'Enter task title',
            'taskDescription': 'Enter task description',
        }

    def __init__(self, *args, **kwargs):
        super(ToDoForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            if field in self.Meta.placeholders:
                self.fields[field].widget.attrs['placeholder'] = self.Meta.placeholders[field]
