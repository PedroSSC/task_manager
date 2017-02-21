from django.shortcuts import render

#Importações para uso de servidor.
from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse

#Classe 'Tarefa' criada.
class Tarefa(object):
    def __init__(self, titulo, data):
        self.titulo = titulo
        self.data = data
    def __str__(self):
        return self.titulo

#Funções de respostas de URL.
def home(request):
    return HttpResponse("Olá!")
def sobre(request):
    return HttpResponse ("Pedro Sousa")
def tarefa(request, numero):
    return HttpResponse("tarefa: " + str(numero))
def tarefa(request, ano, mes):
    return HttpResponse("tarefa: " + str(ano)+"/"+str(mes))
