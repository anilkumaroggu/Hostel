from django.shortcuts import render

from django.http import HttpResponse

def seeit(request):
    return render(request,'web.html')
