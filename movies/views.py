from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        "movies": ['Fall Guy', 'Lord of the Rings', 'Young Guns']
    }
    return render(request,'movies/index.html',context)

def about(request):
    return render(request,'movies/about.html')