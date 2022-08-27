from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Answer, Question, Card, Box, Subject


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(Card)
admin.site.register(Box)
admin.site.register(Subject)
