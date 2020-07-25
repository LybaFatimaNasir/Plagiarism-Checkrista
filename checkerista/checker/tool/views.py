from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import text



def index(request):
    return render(request,'tool.html')

def addText(request):
    try:
        newItem =  text(Content=request.POST['Content'])
        newItem.save()
    except KeyError:
        newItem = "Guest"
    return HttpResponseRedirect('/tool/' )

#newItem= text(Content=c)
#def getData(request): 
    # dictionary for initial data with  
    # field names as keys 
  #  context ={} 
  
    
   # context["dataset"] = text.objects.all() 
    
          
   # return render(request, "tool.html", context)     

# Create your views here.