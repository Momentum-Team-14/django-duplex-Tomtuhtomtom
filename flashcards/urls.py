from sqlite3 import adapt
from django.urls import path
from . import views

# add urlpatterns for directories after the app name directory here
# example for this project 127.0.0.1:*000/flashcards/create this directory here
urlpatterns = [
    path('', views.index, name='index'),
    path('answer/<int:pk>', views.AnswerDetailView.as_view(), name='answer-detail'),
    path('question/<int:pk>', views.QuestionDetailView.as_view(), name='question-detail'),
    path('card/<int:pk>', views.CardDetailView.as_view(), name='card-detail'),
    path('box/<int:pk>', views.BoxDetailView.as_view(), name='box-detail'),
    path('subjects/', views.SubjectListView.as_view(), name='subjects'),
    path('subject/<int:pk>', views.SubjectDetailView.as_view(), name='subject-detail'),
]
