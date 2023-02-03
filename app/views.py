from django.shortcuts import render
from .models import product
def home(request):
    # print(5)
    products=product.objects.all()
    # print(size(products))
    return render(request, 'app/home.html',{'products':products})

def product_detail(request):
 product_id = request.GET.get('query_name')
 i = product.objects.get(id=product_id)
 return render(request, 'app/productdetail.html',{'i':i})

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
 return render(request, 'app/mobile.html')

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')

def topwear(request):
    products=product.objects.all()
    return render(request,'app/topwear.html',{'products':products})

def topwear_product_detail(request):
 product_id = request.GET.get('query_name')
 i = product.objects.get(id=product_id)
 return render(request, 'app/productdetail.html',{'i':i})
