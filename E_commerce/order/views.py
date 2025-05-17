from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView, DetailView
from base.models import Product
from order.models import Cart,Order

# Create your views here.
def add_to_cart(request,pk):
    item = get_object_or_404(Product,pk=pk)
    order_item = Cart.objects.get_or_create(item=item,user=request.user,purchased=False)
    order_qs = Order.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            quantity = request.POST.get('quantity')
            if quantity:
                order_item[0].quantity += int(quantity)
            else:
                order_item[0].quantity += 1
            order_item[0].save()
            return redirect('order:cart')
        else:
            quantity = request.POST.get('quantity', 1)
            order_item[0].quantity = int(quantity)
            order_item[0].save()
            order.orderitems.add(order_item[0])
            return redirect('order:cart')
    else:
        order = Order(user=request.user)
        order.save()
        quantity = request.POST.get('quantity', 1)
        order_item[0].quantity = int(quantity)
        order_item[0].save()
        order.orderitems.add(order_item[0])
        return redirect('order:cart')
    
def cart_view(request):
    carts = Cart.objects.filter(user=request.user,purchased=False)
    orders = Order.objects.filter(user=request.user,ordered=False)
    if carts.exists() and orders.exists():
        order =orders[0]
        context={
            'carts': carts,
            'order': order
        }
        return render(request,'base/cart.html',context)
    else:
        return render(request,'base/cart.html')

def remove_item_from_cart(request, pk):
    item = get_object_or_404(Product,pk = pk)
    orders = Order.objects.filter(user=request.user,ordered =False)
    if orders.exists():
        order = orders[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Cart.objects.filter(item=item,user=request.user,purchased=False)[0]
            order.orderitems.remove(order_item)
            order_item.delete()
            return redirect('order:cart')
        else:
            return redirect('order:cart')
    else:
        return redirect('order:cart')