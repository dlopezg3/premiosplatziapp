from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect # Creación de la clase que permite ejecutar una respuesta http y el response redirect
from django.utils import timezone
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView

from .models import Question, Choice

# Con function based views: 

# def index(request): 
#     latest_question_list = Question.objects.all()
#     context = {
#         "latest_question_list": latest_question_list
#     }
#     return render(request, "polls/index.html", context)


# def detail(request, question_id):
#     # utilizamos el shortcut que da django de get_object_or_404
#     question = get_object_or_404(Question, pk=question_id)
#     context = {
#         "question": question
#     }
#     return render(request, "polls/detail.html", context)

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     context = {
#         "question": question,
#     }
#     return render(request, "polls/results.html", context)


class AboutView(TemplateView):
    template_name = "polls/about.html"

class IndexView(ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        # Return the last five published questions
        return Question.objects.order_by("-pub_date")[:5]
    
class DetailView(DetailView):
    model = Question
    template_name = "polls/detail.html"

class ResultsView(DetailView):
    model = Question

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice  = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        context = {
            "question": question,
            "error_mesage": "No elegiste una respuesta"
        }
        return render(request, "polls/detail.html", context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,))) # Le añadimos una coma al final para indicar que es una tupla de un elemento
    template_name = "polls/results.html"