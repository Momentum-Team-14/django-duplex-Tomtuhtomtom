from django.shortcuts import render
from .models import User, Answer, Question, Card, Box, Subject
from django.views import generic

#When you create a urlpattern in the app urls, create your def and render for it here
# Create your views here.
def index(request):

    return render(request, 'index.html', {})


class AnswerDetailView(generic.DetailView):
    model = Answer

    # def answer(request):
    #     return render(request, 'answer_detail.html', {})


class QuestionDetailView(generic.DetailView):
    model = Question


class CardDetailView(generic.DetailView):
    model = Card


class BoxDetailView(generic.DetailView):
    model = Box


class SubjectListView(generic.ListView):
    model = Subject


class SubjectDetailView(generic.DetailView):
    model = Subject
