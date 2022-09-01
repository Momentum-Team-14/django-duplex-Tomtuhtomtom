from django.contrib.auth.models import AbstractUser as BaseUser
from django.db import models
from django.urls import reverse


NUM_BOXES = 3
BOXES = range(1, NUM_BOXES + 1)


class User(BaseUser):
    pass


class Subject(models.Model):

    def __str__(self):
        return self.title


class Card(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    box = models.IntegerField(
        choices=zip(BOXES, BOXES),
        default=BOXES[0],
    )
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

    def move(self, solved):
        new_box = self.box + 1 if solved else BOXES[0]

        if new_box in BOXES:
            self.box = new_box
            self.save()

        return self
