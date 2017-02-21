from django.shortcuts import render

from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse

def home(request):
    return HttpResponse("Olá!")
def sobre(request):
    return HttpResponse ("Pedro Sousa")
def tarefa(request, numero):
    return HttpResponse("tarefa: " + str(numero))
def tarefa(request, ano, mes):
    return HttpResponse("tarefa: " + str(ano)+"/"+str(mes))
