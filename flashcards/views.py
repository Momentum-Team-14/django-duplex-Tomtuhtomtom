from django.shortcuts import render
from .models import User

#When you create a urlpattern in the app urls, create your def and render for it here
# Create your views here.
def index(request):

    context = {}

    return render(request, 'index.html', context=context)
