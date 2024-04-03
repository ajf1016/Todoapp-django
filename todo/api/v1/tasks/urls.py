
from django.urls import path,include
from api.v1.tasks import views

urlpatterns = [
    path('', views.tasks),
]
