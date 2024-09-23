from django.shortcuts import render
import requests
import sys
from subprocess import run,PIPE

def external(request):
    inp=request.POST.get('form-control')

    out=run(sys.executable,['//C://Users//Jaynam.Shah//Documents//shruproj//MalwareProject_Msc//Extract//url_main.py',inp],shell=False,stdout=PIPE)
    print(out)
    return render(request,'index.html',{'data1':out.stdout})