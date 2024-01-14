from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Product
from django.http import HttpResponsePermanentRedirect


def index(request):
    product_list = Product.objects.all()
    return render(request, 'index.html', context={
		'product_list':product_list
    })

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("index")

def delete_post(request):
    if request.method == 'POST':
        prod_id = request.POST.get('prod_id')
        user_id = request.POST.get('user_id')
        Product.objects.filter(id=prod_id).delete()
        return HttpResponsePermanentRedirect(f'/user_page/{user_id}/')
	
def user_page(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        user = User.objects.get(id=id)
        Product.objects.create(user=user, name=name, price=price, image=image)
        return redirect('index')
    product_list = Product.objects.filter()
    return render(request, 'user_page.html', context={
		'product_list':product_list
    })