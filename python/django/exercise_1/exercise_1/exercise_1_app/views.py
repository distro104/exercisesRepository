from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    my_dict = {'inside_me': "Hello i m from views.py!"}
    return render(request, 'index.html', context=my_dict)
