from django.shortcuts import render,HttpResponse,redirect
from  new_member .models import *
# Create your views hed

def dashboard(request):
    return render(request, 'dashboard/index.html')

def new_user(request):
    member = NewMember.objects.all()
    context = {
        'member':member
    }
    return render(request, 'dashboard/new_user.html',context)

def userdetails(request,newuser_id):
    ud = NewMember.objects.get(id=newuser_id)
    return render(request, 'dashboard/new_userd_detail.html',{'ud':ud})
    
def removeuser(request,newuser_id):
    remove = NewMember.objects.get(id=newuser_id)
    remove.delete()
    return redirect('new_user')