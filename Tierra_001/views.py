from django.shortcuts import render
from .models import foto


def archivo(request):
    index = foto.objects.all()
    context = {
        'index': index
    }
    return render(request, 'archive.html', context)


def selfo(request):
    return render(request, 'About.html')


def trabajos(request):
    return render(request, 'Work.html')


def escrit(request):
    return render(request, 'Notebook.html')

def trabajos1(request):
    return render(request, 'Work-CyberAdv.html')

def trabajos2(request):
    return render(request, 'Work-TechCon.html')