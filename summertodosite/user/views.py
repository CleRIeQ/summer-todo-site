from django.shortcuts import get_object_or_404, redirect
from django.views.generic import  FormView, DeleteView, View
from requests import request
from .forms import CreateGoalForm
from django.core.paginator import Paginator
from .models import goal


class MyGoalsView(FormView):
    model = goal
    template_name = "interface/my_goals.html"
    context_object_name = 'user'
    form_class = CreateGoalForm
    success_url = '/my-goals/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        goals = goal.objects.filter(executor = self.request.user.id)
        paginator = Paginator(goals, 5)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        page_list = []
        for i in range(page_obj.paginator.num_pages):
            i+=1
            page_list.append(i)

        context['user_goals'] = goals
        context['page_obj'] = page_obj
        context['page_list'] = page_list
        return context

    def form_valid(self, form):
        form = form.save(commit=False)
        form.executor = self.request.user
        form.save()
        return super(MyGoalsView, self).form_valid(form)

class GoalsDeleteView(DeleteView):
    model = goal
    template_name = "interface/goal_delete.html"
    context_object_name = 'goal'
    success_url = "/"
    
class GoalsFinishView(View):
    model = goal
    template_name = "interface/goal_finish.html"
    context_object_name = 'goal'
    success_url = '/'

    def get(self, *args, **kwargs):
        pk = self.kwargs['pk']
        post = get_object_or_404(goal, pk=pk)
        post.status = 'Finished'
        post.save()
        return redirect("/my-goals/")

