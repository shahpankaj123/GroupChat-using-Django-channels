from django.shortcuts import render

# Create your views here.
def home(request,group_name):
    return render(request,'index.html',{'g_name':group_name})
