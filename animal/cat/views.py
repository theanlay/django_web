from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html'),
def section1(request):
    return render(request, 'section1.html'),
def section2(request):
    return render(request, 'section2.html')
