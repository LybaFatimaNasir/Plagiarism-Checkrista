from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import text

def results(request):

    objCount = text.objects.all() #count of all  the objects present
    
    stu = {
        'all_Is' : objCount
    }

    return render(request,'results.html', stu)
    #for p in text.objects.raw('Select * from tool_text'):
     #print (p)
    #{'res' : stu}
    #return render (request,'result.html')




def index(request):
    return render(request,'tool.html')

def addText(request):
    try:
        newItem =  text(Content=request.POST['Content'])
        newItem.save()
    except KeyError:
        newItem = "Guest"
    return HttpResponseRedirect('/tool/' )


##########








 #yourData= {'lastcar':  lastText}


    #temp = [None] * objCount #declare temporary array
    #for i in objCount
     #   temp[i]=all_obj[i].Content #storing all objects in array


 # def dectectingPlagiarism(request):

   
          

   # context["dataset"] = text.objects.all() 
    
          
   # return render(request, "tool.html", context)     

# Create your views here.