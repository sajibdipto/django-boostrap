from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    # return HttpResponse("come on baby")
    context = {'name': 'Harry','course':'Django'}
    return render(request,'home.html',context)

def about(request):
        return render(request,'about.html')
    # return HttpResponse("come on baby")
    #context = {'name': 'Harry','course':'Django'}
    

def projects(request):
        return render(request,'projects.html')
    # return HttpResponse("come on baby")
    #context = {'name': 'Harry','course':'Django'}
    

def contact(request):
    if request.method=="POST":
        name= request.POST['name']
        email= request.POST['email']
        phone= request.POST['phone']
        desc= request.POST['desc']
        #print(name, email, phone, desc)
        contact =Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        print("The data has been written to the db")

    return render(request,'contact.html')
    # return HttpResponse("come on baby")
    #context = {'name': 'Harry','course':'Django'}
    