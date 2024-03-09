# from django.shortcuts import render,redirect
# from django.urls import reverse
# from django.conf import settings
# from paypal.standard.forms import PayPalPaymentsForm
# from .models import Donation

# # Create your views here.
# def donation(request):


from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render, redirect
from paypal.standard.forms import PayPalPaymentsForm

def donation (request):
    host= request.get_host()

    # What you want the button to do.
    paypal_dict = {
        "business": "receiver_email@example.com",
        "amount": "10.00",
        "item_name": "donations",
        # "invoice": "unique-invoice-id",
        # "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
        # "return": request.build_absolute_uri(reverse('your-return-view')),
        # "cancel_return": request.build_absolute_uri(reverse('your-cancel-view')),
        # "custom": "premium_plan",  # Custom command to correlate to some function later (optional)

        'invoice': str(donation.id),
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host,
                                           reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host,
                                           reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format(host,
                                              reverse('payment_cancelled')),
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render(request, "payment.html", context)



def paypal_return(request):
    messages.success(request,'You have successfully made a donation!')
    return redirect('payment')

def paypal_cancel(request):
    messages.error(request,'Your payment has been cancelled')
    return redirect('payment')

