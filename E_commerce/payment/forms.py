from django import forms
from .models import BillingAddress

class BillingAddressForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        fields = ['first_name' , 'last_name' , 'country' , 'address1' , 'address2' , 'city' , 'zipcode' , 'phone_number']

