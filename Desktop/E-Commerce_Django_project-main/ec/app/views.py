from django.shortcuts import render,redirect
from django.views import View
from django.db.models import Count
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Product, Customer,Cart
from django.http import JsonResponse
from django.db.models import Q
from .forms import (
    CustomerRegistrationForm,
    LoginForm,
    MyPasswordResetForm,
    CustomerProfileForm
)

# Home page view
def home(request):
    return render(request, "app/home.html")

# About page view
def about(request):
    return render(request, "app/about.html")

# Contact page view
def contact(request):
    return render(request, "app/contact.html")

# View to display products by category
class CategoryView(View):
    def get(self, request, val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values("title")
        return render(request, "app/category.html", locals())

# View to display products by title within a category
class CategoryTitle(View):
    def get(self, request, val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values("title")
        return render(request, "app/category.html", locals())

# View to display product details
class ProductDetail(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, "app/productdetail.html", locals())

# Customer registration view
class CustomerResistrationaView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, "app/customerregistration.html", locals())

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! Successfully Registered.")
        else:
            messages.warning(request, "Invalid Input Data")
        return render(request, "app/customerregistration.html", locals())

# Profile view for displaying and saving user profile
class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, "app/profile.html", locals())

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=user, name=name, locality=locality, city=city,mobile=mobile, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, "Congratulations! Profile Saved Successfully.")
        else:
            messages.warning(request, "Invalid Input Data")
        return render(request, 'app/profile.html', locals())

# View to display user addresses
def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html', locals())
class updateAddress(View):
    def get(self,request,pk):
        add = Customer.objects.get(pk=pk)
        form=CustomerProfileForm(instance=add)
        return render(request, 'app/updateAddress.html', locals())
    def post(self,request,pk):
        form=CustomerProfileForm(request.POST)
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add=Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.state = form.cleaned_data['state']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()
            messages.success(request, "Congratulations! Profile Updated Successfully.")
        else:
            messages.warning(request, "Invalid Input Data")

        return redirect("address")

# Login view
def LoginView(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully logged in.")
                return redirect('home')  # Redirect to the homepage after login
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid input.")
    
    else:
        form = LoginForm()
    
    return render(request, "app/login.html",locals())
def add_to_cart(request):
    user=request.user 
    product_id=request.GET.get('prod_id')
    product=Product.objects.get(id=product_id)
    Cart(user=user,product=product).save()
    return redirect('/cart')
def show_cart(request):
    user=request.user 
    cart=Cart.objects.filter(user=user)
    amount=0
    for p in cart:
        value=p.quantity*p.product.discounted_price
        amount=amount+value
    totalamount=amount+40
    return render(request,'app/addtocart.html',locals())

class checkout(View):
    def get(self,request):
        user=request.user 
        add=Customer.objects.filter(user=user)
        cart_items=Cart.objects.filter(user=user)
        famount=0
        for p in cart_items:
            value=p.quantity*p.product.discounted_price
            famount=famount+value
        totalamount=famount+40
        return render(request,'app/checkout.html',locals())

def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()

        # Recalculating amount and totalamount after updating quantity
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount += value
        totalamount = amount + 40  # Including shipping charges

        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount,
        }
        return JsonResponse(data)

def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))

        if c.quantity > 1:
            c.quantity -= 1
            c.save()
        else:
            c.delete()  # If quantity becomes 0, remove the item from the cart

        # Recalculating amount and totalamount after updating quantity
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount += value
        totalamount = amount + 40  # Including shipping charges

        data = {
            'quantity': c.quantity if c.quantity > 0 else 0,
            'amount': amount,
            'totalamount': totalamount,
        }
        return JsonResponse(data)

def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        
        # Filter the cart items by product ID and user
        carts = Cart.objects.filter(Q(product_id=prod_id) & Q(user=request.user))
        
        # Ensure we have at least one matching cart item
        if carts.exists():
            # Remove all matching cart items
            carts.delete()
            # Calculate the new cart amount and total amount
            user = request.user 
            cart_items = Cart.objects.filter(user=user)
            amount = sum(item.quantity * item.product.discounted_price for item in cart_items)
            totalamount = amount + 40
            data = {
                'quantity': 0,  # No items left, so quantity is 0
                'amount': amount,
                'totalamount': totalamount
            }
        else:
            data = {
                'quantity': 0,
                'amount': 0,
                'totalamount': 40
            }
        
        return JsonResponse(data)