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
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
            cart.clear() #clear cart
            return render(request, 'orders/order/complete.html', {'order':order})
        

    else: #GET request
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart': cart, 'form':form})



    
