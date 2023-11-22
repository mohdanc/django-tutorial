'''polls/views'''
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Question, Choice

def index(request: HttpRequest):
    '''Index view'''
    latest_question_list = Question.questions_qs.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request: HttpRequest, question_id: int) -> HttpResponse:
    '''Shows the detail of a question'''
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def results(request:HttpRequest, question_id: int) -> HttpResponse:
    '''Shows the polls result'''
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/result.html", {"question": question})

def vote(request: HttpRequest, question_id: int) -> HttpResponse:
    '''Votes'''
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render (
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice",
            }
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
