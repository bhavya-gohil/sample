from django.shortcuts import render
from .models import Site

# Create your views here.
def site_detail_view(request):
	obj = Site.objects.get(id=1)
	context = {
		'title': obj.title,
		'desc': obj.desc,
	}
	return render(request,"site/detail.html",context)