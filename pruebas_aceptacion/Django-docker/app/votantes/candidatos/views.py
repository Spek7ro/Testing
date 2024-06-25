from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Candidato, Votacion
from django.db.models import Count

class ListaCandidatos(ListView):
    model = Candidato

def NuevoVoto(request, candidato_id):
    candidato = Candidato.objects.get(id=candidato_id)
    Votacion.objects.create(candidato=candidato)
    return redirect('resultados')    

def ListaResultados(request):
    resultados = Candidato.objects.annotate(votos=Count('votacion'))
    return render(request, 'resultados.html', {'resultados': resultados})
