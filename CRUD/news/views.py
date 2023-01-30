from django.shortcuts import render,redirect
from .models import News
from .forms import newsform

# Create your views here.
def create(request):
    Cnews=newsform()
    if request.method=="POST":
        Cnews=newsform(request.POST,request.FILES)
        if Cnews.is_valid:
            Cnews.save()
        return redirect("/")
    
    context={
        "Cnews":Cnews
    }
    return render(request,"create/create.html",context)

def show(request):
    Snews=News.objects.all()
    context={
        "Snews":Snews,
    }
    return render(request,"show/show.html",context)

def read(request,pk):
    Rnews=News.objects.get(id=pk)
    context={
        "Rnews":Rnews,
    }
    return render(request,"read/read.html",context)


def update(request,pk):
    news=News.objects.get(id=pk)
    Unews=newsform(instance=news)
    if request.method=="POST":
        Unews=newsform(request.POST,request.FILES,instance=news)
        if Unews.is_valid:
            Unews.save()
        return redirect("/")
    
    context={
        "Unews":Unews
    }
    return render(request,"update/update.html",context)


def delete(request,pk):
    Dnews=News.objects.get(id=pk)
    if request.method=="POST":
        Dnews.delete()
        return redirect("/")
    context={
        "Dnews":Dnews,
    }
    return render(request,"delete/delete.html",context)

