from django.forms import ModelForm, CharField
from .models import goal

class CreateGoalForm(ModelForm):
    class Meta:
        model = goal
        fields = ['title', 'priority', ]
    