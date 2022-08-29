from django.shortcuts import render
from .models import User, Answer, Question, Card, Box, Subject
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

#When you create a urlpattern in the app urls, create your def and render for it here
# Create your views here.
def index(request):

    return render(request, 'index.html', {})


class AnswerListView(generic.ListView):
    model = Answer
    
    
class AnswerDetailView(generic.DetailView):
    model = Answer


class AnswerCreate(CreateView):
    model = Answer
    fields = ['answer_content']


class AnswerUpdate(UpdateView):
    model = Answer
    fields = ['answer_content']


class AnswerDelete(DeleteView):
    model = Answer
    success_url = reverse_lazy('answers')

class QuestionListView(generic.ListView):
    model = Question


class QuestionDetailView(generic.DetailView):
    model = Question


class QuestionCreate(CreateView):
    model = Question
    fields = ['question_content']


class QuestionUpdate(UpdateView):
    model = Question
    fields = ['question_content']


class QuestionDelete(DeleteView):
    model = Question
    success_url = reverse_lazy('questions')


class CardListView(generic.ListView):
    model = Card


class CardDetailView(generic.DetailView):
    model = Card


class CardCreate(CreateView):
    model = Card
    fields = ['question', 'answer']


class CardUpdate(UpdateView):
    model = Card
    fields = ['question', 'answer']


class CardDelete(DeleteView):
    model = Card
    success_url = reverse_lazy('cards')

class BoxListView(generic.ListView):
    model = Box
    
    
class BoxDetailView(generic.DetailView):
    model = Box


class BoxCreate(CreateView):
    model = Box
    fields = ['name', 'cards']


class BoxUpdate(UpdateView):
    model = Box
    fields = ['name', 'cards']


class BoxDelete(DeleteView):
    model = Box
    success_url = reverse_lazy('boxes')


class SubjectListView(generic.ListView):
    model = Subject


class SubjectDetailView(generic.DetailView):
    model = Subject


class SubjectCreate(CreateView):
    model = Subject
    fields = ['name', 'boxes']


class SubjectUpdate(UpdateView):
    model = Subject
    fields = ['name', 'boxes']


class SubjectDelete(DeleteView):
    model = Subject
    success_url = reverse_lazy('subjects')


def showAnswer():
    pass

def hideAnswer():
    pass