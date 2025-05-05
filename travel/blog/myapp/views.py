from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def freeport(request):
    return render(request, 'freeport.html')

def law(request):
    return render(request, 'law.html')

def museo(request):
    return render(request, 'museo.html')

def bsp(request):
    return render(request, 'bsp.html')

def hytec(request):
    return render(request, 'hytec.html')

def lrt(request):
    return render(request, 'lrt.html')

def mmda(request):
    return render(request, 'mmda.html')