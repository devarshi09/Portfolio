from django.shortcuts import render

def homepage(request):
	return render(request,'homepage.html')

def about(request):
	return render(request,'about.html')

def skills(request):
	return render(request,'skills.html')

def edu(request):
	return render(request,'Education.html')

def exp(request):
	return render(request,'exp.html')

def ach(request) :
	return render(request,'ach.html')

def certi(request) :
	return render(request,'certi.html')