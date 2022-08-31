from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Card, Subject


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Card)
admin.site.register(Subject)
