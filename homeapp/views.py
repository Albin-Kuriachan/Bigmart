from django.shortcuts import render, redirect

from backend.models import categorydb, productdb
from homeapp.models import regdb, Cartdb, Checkout


# Create your views here.
def homepage(req):
    data = categorydb.objects.all()
    return render(req, "home.html", {'data': data})


def aboutus(req):
    data = categorydb.objects.all()
    return render(req, "aboutus.html", {'data': data})


def contactus(req):
    data = categorydb.objects.all()
    return render(req, "contactus.html", {'data': data})


def pro(req, catname):
    data = categorydb.objects.all()
    cat = productdb.objects.filter(Category=catname)
    return render(req, "propage.html", {'cat': cat, 'data': data})


def singleproduct(req, proid):
    data = categorydb.objects.all()
    cat = productdb.objects.get(id=proid)
    return render(req, "singleproduct.html", {'cat': cat, 'data': data})


def register(req):
    return render(req, "register.html")


def loginpg(req):
    return render(req, "login.html")


def registersave(req):
    if req.method == "POST":
        un = req.POST.get('username')
        en = req.POST.get('email')
        ps = req.POST.get('password')
        img = req.FILES['image']
        obj = regdb(Username=un, Email=en, Password=ps, Image=img)
        obj.save()
        return redirect(loginpg)


def userlogin(request):
    if request.method == "POST":
        user = request.POST.get('username')
        pwd = request.POST.get('password')
        if regdb.objects.filter(Username=user, Password=pwd).exists():
            request.session['username'] = user
            request.session['password'] = pwd
            return redirect(homepage)
        else:
            return redirect(loginpg)
    else:
        return redirect(loginpg)


def logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(homepage)


def cartsave(req):
    if req.method == "POST":
        us = req.POST.get('username')
        pr = req.POST.get('productname')
        qt = req.POST.get('qty')
        tp = req.POST.get('totalprice')
        obj = Cartdb(Username=us, ProductName=pr, Quantity=qt, Total=tp)
        obj.save()
        return redirect(cartdisplay)


def cartdisplay(request):
    data = Cartdb.objects.filter(Username=request.session['username'])
    cat = categorydb.objects.all()
    total_price = 0
    for i in data:
        total_price = total_price + i.Total
    return render(request, "cartdisplay.html", {'data': data, 'cat': cat, 'totalprice': total_price})


def cartdel(req, dataid):
    data = Cartdb.objects.filter(id=dataid)
    data.delete()
    return redirect(cartdisplay)


def checkout(request):
    cat = categorydb.objects.all()
    data = Cartdb.objects.filter(Username=request.session['username'])
    total_price = 0
    for i in data:
        total_price = total_price + i.Total
    return render(request, "checkout.html", {'cat': cat, 'data': data, 'totalprice': total_price})


def checksave(request):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        add = request.POST.get('address')
        ph = request.POST.get('phone')
        obj = Checkout(C_Name=na, C_Email=em, C_Address=add, C_Phone=ph)
        obj.save()
        return redirect(homepage)
