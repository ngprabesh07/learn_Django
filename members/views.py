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