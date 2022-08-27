from django.shortcuts import render
from .models import User, Answer, Question, Card, Box, Subject
from django.views import generic

#When you create a urlpattern in the app urls, create your def and render for it here
# Create your views here.
def index(request):

    return render(request, 'index.html', {})


class AnswerListView(generic.ListView):
    model = Answer
    
    
class AnswerDetailView(generic.DetailView):
    model = Answer

    # def answer(request):
    #     return render(request, 'answer_detail.html', {})


class QuestionListView(generic.ListView):
    model = Question


class QuestionDetailView(generic.DetailView):
    model = Question


class CardListView(generic.ListView):
    model = Card


class CardDetailView(generic.DetailView):
    model = Card


class BoxListView(generic.ListView):
    model = Box
    
    
class BoxDetailView(generic.DetailView):
    model = Box


class SubjectListView(generic.ListView):
    model = Subject


class SubjectDetailView(generic.DetailView):
    model = Subject
