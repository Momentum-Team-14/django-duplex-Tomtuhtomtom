from sqlite3 import adapt
from django.urls import path
from . import views

# add urlpatterns for directories after the app name directory here
# example for this project 127.0.0.1:*000/flashcards/create this directory here
urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += [
    path('answers/', views.AnswerListView.as_view(), name='answers'),
    path('answer/<int:pk>', views.AnswerDetailView.as_view(), name='answer-detail'),
    path('answer/create/', views.AnswerCreate.as_view(), name='answer-create'),
    path('answer/<int:pk>/update/', views.AnswerUpdate.as_view(), name='answer-update'),
    path('answer/<int:pk>/delete/', views.AnswerDelete.as_view(), name='answer-delete'),
]

urlpatterns += [
    path('questions/', views.QuestionListView.as_view(), name='questions'),
    path('question/<int:pk>', views.QuestionDetailView.as_view(), name='question-detail'),
    path('question/create/', views.QuestionCreate.as_view(), name='question-create'),
    path('question/<int:pk>/update/', views.QuestionUpdate.as_view(), name='question-update'),
    path('question/<int:pk>/delete/', views.QuestionDelete.as_view(), name='question-delete'),
]

urlpatterns += [
    path('cards/', views.CardListView.as_view(), name='cards'),
    path('card/<int:pk>', views.CardDetailView.as_view(), name='card-detail'),
    path('card/create/', views.CardCreate.as_view(), name='card-create'),
    path('card/<int:pk>/update/', views.CardUpdate.as_view(), name='card-update'),
    path('card/<int:pk>/delete/', views.CardDelete.as_view(), name='card-delete'),
]

urlpatterns += [
    path('boxes/', views.BoxListView.as_view(), name='boxes'),
    path('box/<int:pk>', views.BoxDetailView.as_view(), name='box-detail'),
    path('box/create/', views.BoxCreate.as_view(), name='box-create'),
    path('box/<int:pk>/update/', views.BoxUpdate.as_view(), name='box-update'),
    path('box/<int:pk>/delete/', views.BoxDelete.as_view(), name='box-delete'),
]

urlpatterns += [
    path('subjects/', views.SubjectListView.as_view(), name='subjects'),
    path('subject/<int:pk>', views.SubjectDetailView.as_view(), name='subject-detail'),
    path('subject/create/', views.SubjectCreate.as_view(), name='subject-create'),
    path('subject/<int:pk>/update/', views.SubjectUpdate.as_view(), name='subject-update'),
    path('subject/<int:pk>/delete/', views.SubjectDelete.as_view(), name='subject-delete'),
]
