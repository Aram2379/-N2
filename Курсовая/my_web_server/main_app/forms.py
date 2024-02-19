from .models import Tasks
from django.forms import ModelForm, TextInput, Textarea, DateInput

class TaskForm(ModelForm):
    class Meta:
        model = Tasks
        fields = ["title", "task"]
        widgets ={
            "title": TextInput(attrs={
                "class": 'form-control',
                "placeholder": 'Введите название'
            }),
            "task": Textarea(attrs={
                "class": 'form-control',
                "placeholder": 'Введите описание'
            }),
            "deadline": DateInput(attrs={
                "class": 'form-control',
                "placeholder": 'Введите дедлайн'
            }),

        }