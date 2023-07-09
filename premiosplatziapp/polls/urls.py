from django.urls import path
from . import views # del paque polls importame views

app_name = "polls"
urlpatterns = [
    # Con function classes
    # path("", views.index, name="index"),
    # ex: /polls
    # path("<int:question_id>/Cambio-URL", views.detail, name="detail"),
    # ex: /polls/5
    # path("<int:question_id>/results", views.results, name="results"),
    # ex: /polls/5/results
    path("<int:question_id>/vote", views.vote, name="vote"),
    # ex: /polls/5/vote

    # Con Generic Clases
    # path("about/", TemplateView.as_view(template_name="about.html")),

    path("about/", views.AboutView.as_view(), name="about"),
    path("", views.IndexView.as_view(), name= "index"),
    path("<int:pk>/detail", views.DetailView.as_view(), name= "detail"),
    path("<int:pk>/results", views.ResultsView.as_view(), name= "results"),
]
