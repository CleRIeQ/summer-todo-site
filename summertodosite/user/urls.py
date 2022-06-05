from django.shortcuts import redirect
from django.urls import include, path
from .views import GoalsDeleteView, MainRedirectView, MyGoalsView, GoalsFinishView

urlpatterns = [
    path('', MainRedirectView.as_view()),
    path('authentication/', include('allauth.urls')),
    path('my-goals/', MyGoalsView.as_view()),
    path('goal-delete/<int:pk>/', GoalsDeleteView.as_view(), name='goal-delete'),
    path('goal-finish/<int:pk>/', GoalsFinishView.as_view(), name='goal-finish'),

]