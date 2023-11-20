from django.shortcuts import render

# Create your views here.

def condition(request):
    d={'a':100,'b':300,'c':200}
    return render(request,'conditional.html',d)
