from django.shortcuts import render
from .models import *

# Create your views here.
def home(request,group_name):
    group=Group.objects.filter(g_name=group_name).first()
    chat_mess=[]
    if group:
        chat_mess=chat.objects.filter(group=group)
        
    else:
        Group.objects.create(g_name=group_name)

    return render(request,'index.html',{'g_name':group_name,'mess':chat_mess})
