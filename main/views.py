from django.shortcuts import render
from .forms import ExampleForm


# Create your views here.
def contact(request):
	form = ExampleForm()
	return render(request, "main/contact.html", {'form':form})