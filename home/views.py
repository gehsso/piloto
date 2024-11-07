from django.shortcuts import HttpResponse, render

# Create your views here.

#view index
def index(request):
    return render(request,"index.html")

#view sobre
def sobre(request):
   return render(request,"sobre.html")

#view contato
def contato(request):
    return render(request,"contato.html")

#view exibir_item
def exibir_item(request, id):
    return render(request,"exibir_item.html",{'id':id})



