import datetime

from django.test import TestCase
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
        
    def test_was_published_recently_with_so_so_recent_questions(self):
        """ was_published_recently returns false 
        for questions whose pub_date is not that recent """
        time = timezone.now() - datetime.timedelta(hours=24)
        recent_question = Question(pub_date = time)
        self.assertIs(recent_question.was_published_recently(), False)
        
