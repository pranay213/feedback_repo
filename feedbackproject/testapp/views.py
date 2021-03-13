from django.shortcuts import render
from . import forms
# Create your views here.
def thankyou_view(request):
    return render(request,'testingapp/thankyou.html')
def feedback_view(request):
    if request.method=='GET':
        form=forms.FeedBackForm()
        return render(request,'testingapp/vin.html',{'form':form})
    if request.method=='POST':
        form=forms.FeedBackForm(request.POST)
        if form.is_valid():
            print('validation completed...printing feedbackinfo')
            print('Student Name:',form.cleaned_data['name'])
            print('Student Roll No:',form.cleaned_data['rollno'])
            print('Student Email:',form.cleaned_data['email'])
            print('Student FeedBack:',form.cleaned_data['feedback'])
            return thankyou_view(request)

    return render(request,'testingapp/vin.html',{'form':form})
