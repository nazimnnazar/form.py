from django.shortcuts import render,HttpResponsePermanentRedirect
from .forms import NewMemberForm
from django.contrib import messages
# Create your views here.

def new_member(request):
    if request.method == "POST":
        form = NewMemberForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Form is SuccessFully Submited")
            return HttpResponsePermanentRedirect('new_member')
        else:
            return render(request, 'new_member/new_member.html',{'form':form})
    else:
        form = NewMemberForm()
        return  render(request, 'new_member/new_member.html',{'form':form})
