from django.shortcuts import render,redirect
import requests
import sys
from subprocess import run,PIPE
import os
from django.views.decorators.cache import never_cache
# from django.views.decorators.cache import never_cache

@never_cache
def login(request):
    return render(request,'Login.html')
@never_cache
def index(request) :
    return render(request,'index.html')
@never_cache
def search(request) :
    return render(request,'searchTrain.html')

@never_cache
def external(request):
    # os.rmdir("D:\\Sem 3\\dbms project\\backend\\master\\master\\__pycache__")
    inp1 = request.POST.get('from')
    inp2 = request.POST.get('to')
    out = run([sys.executable,'D:\\Sem 3\\dbms project\\backend\\master\\scripts\\search.py',inp1,inp2],shell=False,stdout=PIPE)
    print(out)
    return render(request,'search_result.html')
        
    

def chart(request) :
    out = run([sys.executable,'D:\\Sem 3\\dbms project\\backend\\master\\scripts\\chart.py'],shell=False,stdout=PIPE)
    print(out)
    return render(request,'chart.html')

def home(request) :
    return render(request,'index.html')

def about(request) :
    return render(request,'about.html')

def help(request) :
    return render(request,'help.html')

def status(request) :
    return render(request,'PNRcheck.html')

def live(request) :
    return render(request,'liveTrain.html') 

def t_status(request) :
    inp1 = request.POST.get('tno')
    out = run([sys.executable,'D:\\Sem 3\\dbms project\\backend\\master\\scripts\\livetrain.py',inp1],shell=False,stdout=PIPE)
    print(out)
    return render(request,'train_status.html')      

def pnr(request) :
    inp1 = request.POST.get('pnr')
    out = run([sys.executable,'D:\\Sem 3\\dbms project\\backend\\master\\scripts\\pnr.py',inp1],shell=False,stdout=PIPE)
    print(out)
    return render(request,'pnr_result.html')                  

