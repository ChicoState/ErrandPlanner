from django.shortcuts import render

# Create your views here.

def errands(request):
    return render(request, 'errands.html')