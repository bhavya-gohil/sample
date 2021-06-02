from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	context = {
		"my_name": "Bhavya",
		"my_surname": "Gohil"
	}
	return render(request,"index.html",context)
