from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import text



def index(request):
    return render(request,'tool.html')

def addText(request):
    c = request.POST['Content']
    newItem= text(Content=c)
    newItem.save()
    return HttpResponseRedirect('/tool/')


def getData(request): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    
    context["dataset"] = text.objects.all() 
    
          
    return render(request, "tool.html", context)     

# Create your views here.