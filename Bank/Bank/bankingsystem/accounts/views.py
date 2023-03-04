from django.shortcuts import render
from accounts.models import accountholder
from accounts.form import accountModelForm
from accounts.form import depositModelForm
from accounts.form import amountModelForm
from accounts.models import banktype
from accounts.form import amounttype
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

def homepage(request):
    return render(request, 'index.html')

def logoutuser(request):
    return render(request, 'registration/logout.html')

def Banking(request):
    return render(request, 'accounts/Banking.html')

@login_required
def Deposite(request):
    form = depositModelForm
    depositform = {'form':form}

    if request.method == 'POST':
        form = depositModelForm(request.POST)
        if form.is_valid(): 
            form.save()
            return homepage(request)
    result = banktype.objects.all()
    return render(request, 'accounts/Deposite.html',depositform)

@login_required
def Withdraw(request):
    form = amountModelForm
    withdrawamountform = {'form':form}

    if request.method == 'POST':
        form = amountModelForm(request.POST)
        if form.is_valid(): 
            form.save()
            return homepage(request)
    result = amounttype.objects.all()
    return render(request, 'accounts/Withdraw.html',withdrawamountform)


def Report(request):
    form = accountModelForm
    accountform = {'form':form}

    if request.method == 'POST':
        form = accountModelForm(request.POST)
        if form.is_valid(): 
            form.save()
            return homepage(request)
    return render(request, 'accounts/Report.html',accountform)
 

class MyFirstClassBasedView(View):
    def get(self, request):
        return HttpResponse("<h1>Hello World I'm First Class Based View</h1>")
