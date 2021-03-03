from django.shortcuts import render
from .forms import History_File_Image

# Create your views here.
# взято с https://proglib.io/p/bezopasnaya-zagruzka-izobrazheniy-v-veb-prilozhenii-na-django-2020-05-26

from django.http import HttpResponse

def user_history(request):
	"""Process images uploaded by users"""
	if request.method == 'POST':
		form = History_File_Image(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			# Get the current instance object to display in the template
			img_obj = form.instance
			return render(request, 'History_File.html',  {'form': form, 'img_obj': img_obj})
	else:
		form = History_File_Image()
	return render(request, 'History_File.html', {'form': form})

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
