from django.urls import include, path
from .views import MyGoalsView

urlpatterns = [
    path('authentication/', include('allauth.urls')),
    path('my-goals/', MyGoalsView.as_view()),
]