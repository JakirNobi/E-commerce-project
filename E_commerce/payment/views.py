from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from .models import BillingAddress
from .forms import BillingAddressForm
from order.models import Cart,Order
from django.views.generic import TemplateView
from sslcommerz_python.payment import SSLCSession
from decimal import Decimal
# from user.models import Profile
# Create your views here.

class CheckoutTemplateView(TemplateView):
    def get(self, request, *args, **kwargs):
        saved_address = BillingAddress.objects.get_or_create(user = request.user or None)
        saved_address = saved_address[0]
        form = BillingAddressForm(instance = saved_address)

        context = {
            'billing_address': form,
        }
        return render(request, 'payment/checkout.html',context)


    def post(self, request, *args, **kwargs):
        saved_address = BillingAddress.objects.get_or_create(user = request.user or None)
        saved_address = saved_address[0]
        form = BillingAddressForm(instance = saved_address)
        carts = Cart.objects.filter(user=request.user,purchased=False)
        orders = Order.objects.filter(user=request.user,ordered=False)
        if carts.exists() and orders.exists():
            order =orders[0]
        context={
            'carts': carts,
            'order': order
        }

        if request.method == 'post' or request.method =='POST':
            form = BillingAddressForm(request.POST,instance=saved_address)
            if form.is_valid():
                form.save()
                return render(request,'payment/payment_opts.html',context)

def cash_on_delivery(request):
    saved_address = BillingAddress.objects.get_or_create(user = request.user or None)
    saved_address = saved_address[0]
    
    if not saved_address.is_fully_filled():
        return redirect('payment:checkout')
    
    else:
        order_qs = Order.objects.filter(user=request.user, ordered=False)
        order = order_qs[0]
        order.ordered = True
        order.orderId = order.id
        order.paymentId = 'Cash on Delivery'
        order.save()
        cart_items = Cart.objects.filter(user=request.user, purchased=False)
        for item in cart_items:
            item.purchased = True
            item.save()

        return redirect('base:home')
    
def ssl_commerz(request):
    store_id ='stuff685fece204f18'
    store_pass ='stuff685fece204f18@ssl'
    mypayment = SSLCSession(sslc_is_sandbox=True, sslc_store_id=store_id, sslc_store_pass=store_pass)
    status_url = request.build_absolute_uri(reverse('payment:status'))
    mypayment.set_urls(success_url=status_url, fail_url=status_url, cancel_url=status_url, ipn_url=status_url)
    order_qs = Order.objects.filter(user=request.user, ordered = False)[0]
    order_items = order_qs.orderitems.all()
    order_item_count = order_qs.orderitems.count()
    order_total = order_qs.get_totals()
    current_user = request.user
    billing_address = BillingAddress.objects.filter(user=request.user)[0]


    mypayment.set_product_integration(total_amount=Decimal(order_total), currency='BDT', product_category='Null', product_name=order_items, num_of_item=order_item_count, shipping_method='Courier', product_profile='None')

    mypayment.set_customer_info(name=current_user.profile.full_name, email=current_user.email, address1=billing_address.address1, address2=billing_address.address2, city=current_user.profile.city, postcode=current_user.profile.phone_number, country=current_user.profile.country, phone=current_user.profile.phone_number)

    mypayment.set_shipping_info(shipping_to=current_user.profile.full_name, address=billing_address.address1, city=billing_address.city, postcode=billing_address.zipcode, country=billing_address.country)

    response_data = mypayment.init_payment()
    return redirect(response_data['GatewayPageURL'])



@csrf_exempt
def sslc_status(request):
    if request.method == 'POST' or request.method == 'post':
        payment_data = request.POST
        status = payment_data['status']
        if status == 'VALID':
            val_id = payment_data['val_id']
            tran_id = payment_data['tran_id']

            return HttpResponseRedirect(reverse('payment:sslc_complete',kwargs={'val_id':val_id,'tran_id':tran_id}))


    return render(request,'payment/status.html')

def sslc_complete(request, val_id, tran_id):
    order_qs = Order.objects.filter(user=request.user, ordered= False)
    order = order_qs[0]
    order.ordered = True
    order.orderId = val_id
    order.paymentId = tran_id
    order.save()
    cart_items = Cart.objects.filter(user=request.user, purchased=False)
    for item in cart_items:
        item.purchased = True
        item.save()

    return redirect('base:home')

