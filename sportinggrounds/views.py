from django.shortcuts import render
from django.http import HttpResponse

posts = [{'name': 'Otto-Hahn-Park', 'image': r'C:\Workplace\Meet4Sports\Meet4\sportinggrounds\images\ottohahn.jpg'}, {'name': 'Unisport', 'image': r'C:\Workplace\Meet4Sports\Meet4\sportinggrounds\images\unisport.jpg'}]

def home(request):
    context={
        'posts':posts
    }
    return render(request, 'home.html', context)
