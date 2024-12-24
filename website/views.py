import time
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from . forms import SignUpForm,Addfile
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
def del_file(request,pk):
	if request.user.is_authenticated:
		tar_file=File.objects.get(id=pk)
		tar_file.delete()
		messages.success(request,"You have successfully deleted file")
		return redirect('home')
	else:
		messages.success(request,"You need to logged in")
		return redirect('home')	
def add_file(request):
	addform=Addfile(request.POST or None)
	if request.user.is_authenticated:
		if request.method=="POST":
			if addform.is_valid():
				addform.save()
				messages.success(request,"File added successfully")
				return redirect('home')	
		return render(request,'addfile.html',{'form':addform})		
	else:
		messages.success(request,"You need to logged in")
		return redirect('home')
def update_file(request,pk):
	if request.user.is_authenticated:
		curr_file=File.objects.get(id=pk)
		updateform=Addfile(request.POST or None,instance=curr_file)
		if updateform.is_valid():
			updateform.save()
			messages.success(request,"File updated successfully")
			return redirect('home')	
		return render(request,'updatefile.html',{'form':updateform})	
	else:
		messages.success(request,"You need to logged in")
		return redirect('home')	
