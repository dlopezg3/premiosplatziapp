from django.urls import path
from . import views # del paque polls importame views

urlpatterns = [
    path("", views.index, name="index") #
]
