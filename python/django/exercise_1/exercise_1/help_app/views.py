from django.shortcuts import render
from django.http import HttpResponse


def help(request):
    help_dict = {'help_insert': 'HELP PAGE'}
    return render(request, 'help_app/index.html', context=help_dict)