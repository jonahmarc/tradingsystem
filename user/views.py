from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from user.models import User, Stock, OrderReceipt, MyStock
from .forms import UserForm, MyStockForm


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Invalid User!')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Wrong Password!')
    return render(request, 'user/login.html')

def signupUser(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('login')

    return render(request, 'user/signup.html', {'form': form})

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    print('check!',request.user)
    return render(request, 'user/home.html')

@login_required(login_url='login')
def buyStock(request):
    form = MyStockForm()
    if request.method == 'POST':
        stock_name = request.POST.get('stock_name')
        price = request.POST.get('price')
        purchase_qty = request.POST.get('purchase_qty')
        total = request.POST.get('total')
        stock = Stock.objects.get(name=stock_name)
        stock_qty = stock.quantity - int(purchase_qty)
        if stock is not None:
            try:
                user = User.objects.get(username=request.user)

                mystock = MyStock(
                        user=user,
                        stock=stock, 
                        quantity=int(purchase_qty)
                        )
                mystock.save(force_insert=True)

                Stock.objects.filter(name=stock_name).update(quantity=stock_qty)

                receipt = OrderReceipt(
                        user=user,
                        stock_name=stock_name,
                        price=float(price),
                        quantity=int(purchase_qty),
                        total=float(total),
                        order_type='BUY'
                        )
                receipt.save(force_insert=True)
                return redirect('home')
            except Exception as e:
                messages.error(request, 'An error occured during buying')
        else:
            messages.error(request, 'Stock Not Found')
    
    return render(request, 'user/home.html')


@login_required(login_url='login')
def transactions(request):
    return render(request, 'user/orderhistory.html')