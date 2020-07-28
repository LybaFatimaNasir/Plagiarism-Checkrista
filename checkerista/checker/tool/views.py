from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import text

def results(request):
    return render(request,'result.html' )

def index(request):
    return render(request,'tool.html')

#def result(request):
    #return render(request,'result.html')

def addText(request):
    try:
        newItem =  text(Content=request.POST['Content'])
        newItem.save()
    except KeyError:
        newItem = "Guest"
    return HttpResponseRedirect('/tool/' )

<<<<<<< HEAD


#def getData(request): 
    # dictionary for initial data with  
    # field names as keys 
  #  context ={} 
=======
def addText(request):
    try:
        newItem =  text(Content=request.POST['Content'])
        newItem.save()
    except KeyError:
        newItem = "Guest"
    return HttpResponseRedirect('/tool/' )
>>>>>>> ff55ed2fc1b648bdca237ea2fd2e613d08a82a02
  
    
   # context["dataset"] = text.objects.all() 
    
          
   # return render(request, "tool.html", context)     

# Create your views here.