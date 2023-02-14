from django.shortcuts import render,redirect,HttpResponse
from .models import cateen
from django.urls import reverse
from django.http import HttpResponseRedirect
from itertools import zip_longest as zip
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

prices = []
quantities = []
items = []
def add(request):
    if request.method == "POST":
        value = request.POST.get("item")
        a = request.POST.get("quantity")
        item,price = value.split(" - ₹")
        items.append(item)
        quantities.append(int(a) )
        prices.append(int(price))
        return HttpResponseRedirect("/kiet/mycart")
    return render(request,"kiet/add.html",{
        "cateen": cateen.objects.all(),
        
        
    })

def cart(request):
    if "data" not in request.session:
        request.session["prices"] = {}
    data = list(zip(items,prices,quantities))
    total = 0
    for i,j in zip(prices,quantities):
        total += i*j
    return render(request,"kiet/cart.html",{
        "data": data,
        "total": total
    })
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import User
from django.contrib import messages
def signup(request):
    if request.method == 'POST':
        rollnumber = request.POST['rollnumber']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(rollnumber=rollnumber).exists():
                return render(request,"kiet/signup.html",{'error': 'That username is taken'})
            else:
                user = User.objects.create(rollnumber = rollnumber, password=password)
                user.save()
                return redirect('login')
        else:
            return render(request,"kiet/signup.html",{'error': 'Passwords do not match'})
    else:
        return render(request, 'kiet/signup.html')

from django.contrib.auth import login
from django.shortcuts import render, redirect
from .models import User

def login_view(request):
    if request.method == 'POST':
        rollnumber = request.POST.get('rollnumber')
        password = request.POST.get('password')

        try:
            user = User.objects.get(rollnumber=rollnumber)
        except User.DoesNotExist:
            return render(request, 'kiet/login.html', {'error': 'Invalid user_id'})

        if user.password == password:
            login(request, user)
            return render(request,"kiet/index.html",{
                "cateen": cateen.objects.all()
            })
        else:
            return render(request, 'kiet/login.html', {'error': 'Invalid password'})
    else:
        return render(request, 'kiet/login.html')