from turtle import settiltangle
from django.views.generic import ListView, FormView
from django.views.generic.edit import FormMixin
from requests import request
from .forms import CreateGoalForm

from .models import goal
# Create your views here.

class MyGoalsView(FormView):
    model = goal
    template_name = "interface/my_goals.html"
    context_object_name = 'user'
    form_class = CreateGoalForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        goals = goal.objects.filter(executor = self.request.user.id)

        context['user_goals'] = goals
        return context

    def form_valid(self, form):
        form = form.save(commit=False)
        form.executor = self.request.user
        form.save()
        return super(MyGoalsView, self).form_valid(form)