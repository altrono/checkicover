from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def inquiry(request):
    return render(request, 'main/inquiry.html')

def help(request):
    return render(request, 'main/help.html')

def search(request):
    return render(request, 'main/search.html')