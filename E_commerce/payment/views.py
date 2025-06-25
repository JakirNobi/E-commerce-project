from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import BillingAddress
from .forms import BillingAddressForm
from order.models import Cart,Order
from django.views.generic import TemplateView


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
        if request.method == 'post' or request.method =='POST':
            form = BillingAddressForm(request.POST,instance=saved_address)
            if form.is_valid():
                form.save()
                return redirect('base:home')


