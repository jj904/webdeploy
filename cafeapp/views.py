from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def detail(request):
    return render(request, 'portfolio-details.html')

def detail1(request):
    return render(request, 'portfolio-details1.html')

def detail2(request):
    return render(request, 'portfolio-details2.html')

def detail3(request):
    return render(request, 'portfolio-details3.html')

def detail4(request):
    return render(request, 'portfolio-details4.html')

def detail5(request):
    return render(request, 'portfolio-details5.html')


