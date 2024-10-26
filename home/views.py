from django.shortcuts import HttpResponse, render

# Create your views here.


#view index
def index(request):
    return render(request,"index.html")

#view sobre
def sobre(request):
    return HttpResponse("Sobre o Sistema!")

def contato(request):
    return HttpResponse("Entre em contato")
