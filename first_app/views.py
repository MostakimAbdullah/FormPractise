from django.shortcuts import render
from first_app.django_form import Django_Form

# Create your views here.
def Django_form(request):
    form = Django_Form(request.POST)
    print(form)
    return render(request,'form.html',{'form':form})
    