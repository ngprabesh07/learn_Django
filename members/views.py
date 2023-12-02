from unittest import loader
from django.http import HttpResponse
from django.shortcuts import render

from members.models import Member

# Create your views here.
def members(request):
    mymembers = Member.objects.all().values()
    context= {
        'mymembers': mymembers,
    }
    return render(request,'all_members.html',context)

def details(request, id):
  mymember = Member.objects.get(id=id)
  context = {
    'mymember': mymember,
  }
  return render(request,'details.html',context)

def main(request):
   return render(request,'main.html')

def testing(request):
   context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
   return render(request,'template.html',context)