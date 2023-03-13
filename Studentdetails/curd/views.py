from django.shortcuts import render,redirect

from django.contrib.auth.models import User
from .models import Contact


def index(request):
    Data = Contact.objects.all()
    return render(request,"index2.html",{'Data':Data})


def saveinfo(request):
    if request.method == "POST":
        name=request.POST['name']
        address=request.POST['address']
        phone=request.POST['phone']
        add=Contact(name=name,address=address,phone=phone)
        add.save()

        Data = Contact.objects.all()
        return render(request,"index2.html",{'Data':Data})
    else:
        return render(request,"index2.html")




def formupdate(request,id):
    if request.method=="POST":
        add=Contact.objects.get(id=id)

        add.name=request.POST["name"]
        add.address=request.POST['address']
        add.phone=request.POST['phone']
        add.save()
        return redirect("index")

def edit(request,id):
    Data = Contact.objects.get(id=id)
    return render(request,'edit.html',{'Data':Data})

def delete(request,id):
    add = Contact.objects.get(id=id)
    add.delete()
    return redirect('index') 

# def search(request):
#     query=request.GET["query1"]
#     Data=Contact.objects.filter(phone_icontains=query)
#     params={'Data':Data}
#     return render(request,'search.html',params)       





