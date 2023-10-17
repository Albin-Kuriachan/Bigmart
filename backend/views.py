from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages

from backend.models import categorydb, productdb


# Create your views here.
# index page
def indexpage(req):
    return render(req, "index.html")


# category page
def categorypage(req):
    return render(req, "category.html")


def categorysave(req):
    if req.method == "POST":
        cn = req.POST.get('categoryname')
        dn = req.POST.get('description')
        img = req.FILES['image']
        obj = categorydb(CategoryName=cn, Description=dn, Image=img)
        obj.save()
        messages.success(req,"Category Save Successfully")
        return redirect(categorypage)


def categorydisplay(req):
    data = categorydb.objects.all()
    return render(req, "categorydisplay.html", {'data': data})


def categoryedit(req, dataid):
    data = categorydb.objects.get(id=dataid)
    return render(req, "categoryedit.html", {'data': data})


def categoryupdate(req, dataid):
    if req.method == "POST":
        ct = req.POST.get('categoryname')
        ds = req.POST.get('description')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = categorydb.objects.get(id=dataid).Image
        categorydb.objects.filter(id=dataid).update(CategoryName=ct, Description=ds, Image=file)
        messages.success(req,"Update  Successfully")
        return redirect(categorydisplay)


def categorydelete(req, dataid):
    data = categorydb.objects.filter(id=dataid)
    data.delete()
    messages.warning(req,"Delete Successfully")
    return redirect(categorydisplay)


# product page
def productpage(req):
    cat = categorydb.objects.all()
    return render(req, "product.html", {'cat': cat})


def productsave(req):
    if req.method == "POST":
        ct = req.POST.get('category')
        pn = req.POST.get('productname')
        ds = req.POST.get('description')
        pr = req.POST.get('price')
        img = req.FILES['image']
        obj = productdb(Category=ct, ProductName=pn, Description=ds, Price=pr, Image=img)
        obj.save()
        messages.success(req,"Product Save successfully")
        return redirect(productpage)


def productdisplay(req):
    data = productdb.objects.all()
    return render(req, "productdisplay.html", {'data': data})


def productedit(req, dataid):
    cat = categorydb.objects.all()
    data = productdb.objects.get(id=dataid)
    return render(req, "productedit.html", {'data': data, 'cat': cat})


def productupdate(req, dataid):
    if req.method == "POST":
        ct = req.POST.get('category')
        pn = req.POST.get('productname')
        ds = req.POST.get('description')
        pr = req.POST.get('price')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = productdb.objects.get(id=dataid).Image
        productdb.objects.filter(id=dataid).update(Category=ct, ProductName=pn, Description=ds, Price=pr, Image=file)
        messages.success(req, "Update successfully")
        return redirect(productdisplay)


def productdelete(req, dataid):
    data = productdb.objects.filter(id=dataid)
    data.delete()
    messages.warning(req, "Delete successfully")
    return redirect(productdisplay)


# admin page
def adminpage(req):
    return render(req, "adminpage.html")


def adminsave(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        if User.objects.filter(username__contains=uname).exists():
            user = authenticate(username=uname, password=pwd)
            if user is not None:
                login(request, user)
                request.session['username'] = uname
                request.session['password'] = pwd
                messages.success(request, "Login Successfully")

                return redirect(indexpage)
            else:
                messages.error(request,"Invalid username")
                return redirect(adminpage)

        else:
            messages.error(request,"Invalid Password")
            return redirect(adminpage)


def adminlogut(request):
    del request.session['username']
    del request.session['password']
    messages.success(request,"Logout Successfully")
    return redirect(adminpage)
