from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse("<em>Hello World!!</em>") ## first example

    my_dictionary = {'insert_me': "Hello! I'm from views.py! I have been injected dynamically by django"}
    return render(request, 'first_app/index.html', context=my_dictionary) ## second
    ## there's no need to use the 'os.path.join' function here, because onlsy the browsers are going to interprete this path

def help(request):
    my_dictionary = {'insert_help': "Hello! How an i help you?"}
    return render(request, 'first_app/help.html', context=my_dictionary)