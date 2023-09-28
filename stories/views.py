from django.shortcuts import render, get_object_or_404
from .models import Stories  # Importe o modelo de Story

def lista_stories(request):
    stories = Stories.objects.all()
    return render(request, 'stories/lista_stories.html', {'stories': stories})

def detalhes_stories(request, pk):
    story = get_object_or_404(Stories, pk=pk)
    return render(request, 'stories/detalhes_stories.html', {'stories': story})
