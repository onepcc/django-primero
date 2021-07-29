from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return HttpResponse("placeholder para luego mostrar una lista de todos los blogs <br> <ul><li>blog1</li><li>blog2</li><li>blog3</li></ul>")

# def root(request):
#     return HttpResponse("<h1> ESTO ES UN BLOG</h1> <br> <p> placeholder para luego mostrar una lista de todos los blogs</p>")

def root(request):
    return redirect ("/blogs")

def new(request):
    return HttpResponse("<h1>ESTO ES UN BLOG</h1> <br> <p> placeholder para mostrar un nuevo formulario para crear un nuevo blog</p>")

def create(request):
    return redirect ("/")

def show(request,number):
    return HttpResponse(f"<h1>ESTO ES UN BLOG</h1> <br> <p> placeholder para mostrar el blog numero: {number}</p>")

def edit(request,number):
    return HttpResponse(f"<h1>ESTO ES UN BLOG</h1> <br> <p>placeholder para editar el blog {number}</p>")

def destroy(request,number):
    return redirect ("/")

# def json_test(request):
#     data ={'name':'Poco negro','age':19}
#     import json
#     data_str =json.dumps (data) # Serializar datos en una cadena de formato json
#     return HttpResponse(data_str)


def json_test(request):
    data  =[{"nombre": "Juan", "email": "jp@example.org"}, 
{"name": "Maria", "email": "mari@example.org"}]
    data_str =json.dumps (data) # Serializar datos en una cadena de formato json
    return JsonResponse(data, safe=False)