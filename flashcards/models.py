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
