from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    my_dict = {"insert_me": "Hello i m from views.py in exercise_1_app!"}

    return render(request, 'exercise_1_app/index.html', context=my_dict)
