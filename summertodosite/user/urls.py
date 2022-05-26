from django.urls import include, path

urlpatterns = [
    path('authentication/', include('allauth.urls'))
]