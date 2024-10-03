from django.shortcuts import render
from main.forms import InputForm

def home_view(request):
    context ={}
    context['form']= InputForm()
    return render(request, "main/home.html", context)