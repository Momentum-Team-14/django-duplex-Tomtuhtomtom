from django.contrib.auth.models import AbstractUser as BaseUser
from django.db import models
from django.urls import reverse


# Create your models here.
class User(BaseUser):
    # custom attributes if desired
    pass


class Answer(models.Model):
    answer_content = models.TextField(
        max_length=255,
        help_text='Record answer here'
        )

    def get_absolute_url(self):
        return reverse('answer-detail', args=[str(self.id)])

    def __str__(self):
        return self.answer_content


class Question(models.Model):
    question_content = models.TextField(
        max_length=255,
        help_text='Record question here'
        )

    def get_absolute_url(self):
        return reverse('question-detail', args=[str(self.id)])

    def __str__(self):
        return self.question_content


class Card(models.Model):
    question = models.ForeignKey(
        'Question',
        on_delete=models.CASCADE,
        blank=True, null=True,
        related_name='questions'
        )
    answer = models.ForeignKey(
        'Answer',
        on_delete=models.CASCADE,
        blank=True, null=True,
        related_name='answers'
        )

    def get_absolute_url(self):
        return reverse('card-detail', args=[str(self.id)])

    def __str__(self):
        return f'The question is {self.question} and the answer is {self.answer}'


class Box(models.Model):
    name = models.IntegerField(blank=True, null=True)
    cards = models.ManyToManyField('Card', blank=True, null=True, related_name="boxes")

    class Meta:
        verbose_name_plural = "boxes"

    def get_absolute_url(self):
        return reverse('box-detail', args=[str(self.id)])

    def __str__(self):
        return str(self.name)


class Subject(models.Model):
    name = models.CharField(max_length=200, help_text='Enter Subject')
    boxes = models.ManyToManyField('Box', blank=True, null=True, related_name="subjects")

    def get_absolute_url(self):
        return reverse('subject-detail', args=[str(self.id)])

    def __str__(self):
        return self.name
