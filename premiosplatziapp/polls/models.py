import datetime
import pytz

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.question_text # Cada que invoquemos el metodo queremos que nos muestre el texto de la pregunta
    
    def was_published_recently(self):
        return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=1) # un time delta es un objeto que define diferencia de tiempo


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # Borramos una pregunta se borran las respuestas asociadas
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text # Cada que invoquemos el metodo queremos que nos muestre el texto de la respuesta
