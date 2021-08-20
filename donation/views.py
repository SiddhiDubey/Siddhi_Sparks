from django.shortcuts import render

# Create your views here.
import razorpay
from . models import *

from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, "index.html")



def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        amount = int(request.POST.get('amount')) * 100
        client = razorpay.Client(auth =("rzp_test_WLDv1iDKwLKtPK" , "L9nliUyV6rZXw17HfR1LcZUw"))
        payment = client.order.create({'amount':amount, 'currency':'INR',
                              'payment_capture':'1' })
        
        donate = Donate(name = name, email = email, amount =amount , payment_id = payment['id'])
        


        
        donate.save()
        
        return render(request, 'register.html' ,{'payment':payment})
    return render(request, 'register.html')


@csrf_exempt
def success(request):
    if request.method == "POST":
        a = request.POST
        order_id = ""
        for key, val in a.items():
            if key == 'razorpay_order_id':
                order_id = val
                break
        user = Donate.objects.filter(payment_id = order_id).first()
        user.paid = True
        user.save()

       
    return render(request, "success.html")