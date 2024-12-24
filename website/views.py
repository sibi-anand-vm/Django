import time
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from . forms import SignUpForm
from .models import File
def home(request):
	files=File.objects.all()
	if request.method=="POST":
		username=request.POST['Username']
		password=request.POST['Password']
		user=authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			messages.success(request,"You logged In")
			return redirect('home')
		else:
			messages.success(request,"There is some problem.Please Try again...")
			return redirect('home')
	else:	
		return render(request,'home.html',{'files':files})
def logout_user(request):
	logout(request)
	messages.success(request,"You are logged out.")
	return redirect('home')
def register_user(request):
	if request.method=="POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data['username']
			password=form.cleaned_data['password1']
			user=authenticate(username=username,password=password)
			login(request,user)
			messages.success(request,"You have successfully registered")
			return redirect('home')
	else:
		form=SignUpForm()
		return render(request,'register.html',{'form':form})		
	return render(request,'register.html',{'form':form})
def customer_file(request,pk):
	if request.user.is_authenticated:
		cus_file=File.objects.get(id=pk)
		return render(request,'file.html',{'cus_file':cus_file})
	else:
		messages.success(request,"You need to logged in")
		return redirect('home')	
