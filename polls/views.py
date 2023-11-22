'''polls/views'''
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404
from .models import Question

def index(request: HttpRequest):
    '''Index view'''
    latest_question_list = Question.questions_qs.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request: HttpRequest, question_id: int) -> HttpResponse:
    '''Shows the detail of a question'''
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def results(_:HttpRequest, question_id: int) -> HttpResponse:
    '''Shows the polls result'''
    return HttpResponse(f"You're looking at the result of question {question_id}")

def vote(_: HttpRequest, question_id: int) -> HttpResponse:
    '''Votes'''
    return HttpResponse(f"You're voting for question {question_id}")
