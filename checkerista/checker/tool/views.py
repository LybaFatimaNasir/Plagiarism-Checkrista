from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import text



def index(request):
    return render(request,'tool.html')

def result(request):
    return render(request,'result.html')

def addText(request):
    c = request.POST['Content']
    newItem= text(Content=c)
    newItem.save()
    return HttpResponseRedirect('/tool/')

#def results(request,text_id):
    #response = " Oh there is the result %s."
    #return HttpResponse(response % text_id)

def getData(request): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    
    context["dataset"] = text.objects.all() 
    
          
    return render(request, "tool.html", context)     

# Create your views here.