import datetime

from django.test import TestCase
from django.urls.base import reverse
from django.utils import timezone
from .models import Question

class QuestionModelTest(TestCase):

    def setUp(self):
        self.question = Question(question_text="prueba")

    def test_was_published_recently_with_future_questions(self):
        """ was_published_recently returns false 
        for questions whose pub_date is in the future """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date = time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_questions(self):
        """ was_published_recently returns true 
        for questions whose pub_date is recent """
        time = timezone.now() - datetime.timedelta(hours=23)
        recent_question = Question(pub_date = time)
        self.assertIs(recent_question.was_published_recently(), True)
        
    def test_was_published_recently_with_no_so_recent_questions(self):
        """ was_published_recently returns false 
        for questions whose pub_date is not that recent """
        time = timezone.now() - datetime.timedelta(hours=24)
        recent_question = Question(pub_date = time)
        self.assertIs(recent_question.was_published_recently(), False)
        
class QuestionIndexViewTest(TestCase):

    def test_no_questions(self):
        """When no questions return an appropiate message"""
        response = self.client.get(reverse("polls:index")) # estamos replicando si mandaramos el get request con la url de index de polls y lo guardamos en response
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No existen preguntas disponibles")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    def test_no_future_questions(self):
        time = timezone.now() + datetime.timedelta(days=30)
        Question(question_text="Prueba", pub_date = time).save()

        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No existen preguntas disponibles")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    def test_show_recent_questions(self):
        # self.question = Question(question_text="prueba")
        time = timezone.now() - datetime.timedelta(hours=20)
        Question(question_text="Prueba", pub_date = time).save()

        response = self.client.get(reverse("polls:index"))
        self.assertEqual(len(response.context["latest_question_list"]), 1)

    def test_show_recent_questions_only(self):
        # self.question = Question(question_text="prueba")
        time = timezone.now() - datetime.timedelta(hours=20)
        Question(question_text="recent", pub_date = time).save()

        time = timezone.now() + datetime.timedelta(hours=20)
        Question(question_text="future", pub_date = time).save()

        response = self.client.get(reverse("polls:index"))
        self.assertEqual(len(response.context["latest_question_list"]), 1)
        




