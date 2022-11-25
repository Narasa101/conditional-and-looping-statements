from django.shortcuts import render

# Create your views here.
def a1_first(request):
    d={'a':300,'b':500}
    return render(request,'a1_first.html',d)

def a1_second(request):
    d={'a':100,'b':700,'c':400}
    return render(request,'a1_second.html',d)