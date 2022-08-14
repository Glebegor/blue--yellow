from django.shortcuts import render, redirect
from .models import goodesModel, goodesCountFormModel
from .forms import NewGoodes, ordersForm, RepluuGoodesinfo
from django.core.mail import send_mail
from django.conf import settings
import gspread

# Path to service service_account123.json
sba = gspread.service_account(filename="goods/service_account123.json")
# Name of google spreadsheet
sbh = sba.open("")
# Name of sheet
wbks = sbh.worksheet("")









def goods(request):
    objetsend = goodesModel.objects.all()
    objetsend2 = []
    objlen = len(objetsend)-1
    for i in range(0, objlen):
        objetsend2.append(objetsend[i])
    
    obj2len = len(objetsend2)-1
    for item in objetsend2:
        add = goodesModel.objects.filter(Title=item.Title)
        for itemsadd in add:
            if itemsadd == add[0]:
                pass
            else:
                objetsend2.remove(itemsadd)
    data={
        "Title": "Товари",
        "goodsModel": objetsend2
    }
    return render(request,template_name='orders/orders.html',context=data)

def newGoodesView(request):
    if request.user.is_superuser:
        form = NewGoodes()
        if request.method == "POST":
            form = NewGoodes(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('orders')
        data={
            "Title": "Додати товари",
            "form": form
        }
    else:
        return redirect('home')
    return render(request,template_name='orders/addGoodes.html',context=data)

def GoodesCats(request, cat):
    obj = goodesModel.objects.filter(Title=cat)
    TitleObjects = obj[0].Title
    data = {
            "Title": "Товар: ",
            "goodsModel": obj,
            "TitleObjects": TitleObjects
    }
    return render(request, template_name="orders/CatOrders.html", context=data)

def newGoodesInfo(request, cat, artic):
    obj = goodesModel.objects.filter(Title=cat,article=artic)
    TitleObjects = obj[0]
    data = {
            "Title": "Товар: "+ obj[0].Title,
            "goodsModel": obj,
            "TitleObjects": TitleObjects
    }
    return render(request, template_name="orders/GoodsInfo.html", context=data)

def RecreateNewGoodes(request, id):
    form = RepluuGoodesinfo
    obj = goodesModel.objects.get(id=id)
    if request.method == "POST":
        form = RepluuGoodesinfo(request.POST, request.FILES)
        if form.is_valid():
            obj.Title = form.cleaned_data["Title"]
            obj.version = form.cleaned_data["version"]
            obj.article = form.cleaned_data["article"]
            obj.material = form.cleaned_data["material"]
            obj.furniture = form.cleaned_data["furniture"]
            obj.colors = form.cleaned_data["colors"]
            obj.price = form.cleaned_data["price"]
            obj.imageGoodes = form.cleaned_data["imageGoodes"]
            obj.save()
            return redirect('goodesinfo', cat=obj.Title, artic=obj.article)
    data = {
        "formRepull": form,
        "obj": obj
    }
    return render(request, template_name='orders/RemasteredGoods.html', context=data)

def DeleteNewGoodes(request, id):
    obj = goodesModel.objects.get(id=id)
    obj.delete()
    return redirect('goodesCat', cat=obj.Title)

def OrderOfGoods(request):
    OrdersForm = ordersForm()
    if request.method == "POST":
        OrdersForm = ordersForm(request.POST) 
        if OrdersForm.is_valid():
            formColidddddd = goodesCountFormModel.objects.all()[0]
            formColidddddd.FormCountCol = formColidddddd.FormCountCol + 1
            formColidddddd.save() 
            formColidSh = formColidddddd.FormCountCol 

            nameOrder = OrdersForm.cleaned_data["name"]
            goodsOrder = OrdersForm.cleaned_data["goods"]
            countOrder = OrdersForm.cleaned_data["count"]
            numberOrder = OrdersForm.cleaned_data["number"]
            materialOrder = OrdersForm.cleaned_data["material"]
            brandOrder = OrdersForm.cleaned_data["brand"]
            maketOrder = OrdersForm.cleaned_data["maket"]
            timeOrder = OrdersForm.cleaned_data["time"]
            messageOrder = OrdersForm.cleaned_data["message"]


            wbks.update('A{}'.format(formColidSh), nameOrder)
            wbks.update('B{}'.format(formColidSh), goodsOrder)
            wbks.update('C{}'.format(formColidSh), countOrder)
            wbks.update('D{}'.format(formColidSh), numberOrder)
            wbks.update('E{}'.format(formColidSh), materialOrder)
            wbks.update('F{}'.format(formColidSh), brandOrder)
            wbks.update('G{}'.format(formColidSh), maketOrder)
            wbks.update('H{}'.format(formColidSh), timeOrder)
            wbks.update('I{}'.format(formColidSh), messageOrder)
            wbks.update('J{}'.format(formColidSh), "-")

            return redirect('orders')
    data = {
        'OrdersForm': OrdersForm,
        'Title': 'Замовлення',
    }
    return render(request, template_name="orders/CreateOrderOfGoods.html",context=data)