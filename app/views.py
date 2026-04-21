from django.shortcuts import render
from . import models

# Create your views here.

def start(request):
    # users=[
    #     {'ism':'Saidakbar','familiya':'Afzalxonov','yosh':12}
    # ]

    users=models.User.objects.all() 
    return render(request, 'app/index.html',context={'users':users})
