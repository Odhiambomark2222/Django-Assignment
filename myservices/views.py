from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')
def portfolio(request):
    return render(request,'portfolio-details.html')
def service(request):
    return render(request,'service-details.html')
def stater(request):
    return render(request,'starter-page.html')