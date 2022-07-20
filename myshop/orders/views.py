from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart

# Create your views here.

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save() #save in database
            for item in cart: #create OrderItem object for each item in cart
                OrderItem.objects.create(order, item['[product'], item['price'], item['quantity'])

            #clear cart
            cart.clear()
            return render(request, 'orders/order/completed.html', {'order':order})

    else: #GET request
        form = OrderCreateForm()
    return render(request, 'orders/order/completed.html', {'cart': cart, 'form':form})
