'''Polls models'''
from django.db import models
from django.utils import timezone
from django.urls import reverse

class Question(models.Model):
    '''Question model'''
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(verbose_name="date published")

    questions_qs = models.Manager()

    def was_published_recently(self):
        '''aaa'''
        return self.pub_date >= timezone.now() - timezone.timedelta(days=1)

    def __str__(self) -> str:
        return str(self.question_text)

class Choice(models.Model):
    '''Choice model'''
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return str(self.choice_text)
