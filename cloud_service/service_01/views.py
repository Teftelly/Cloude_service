from .models import User_History
from . import TEST_RUNNER # показывает, как должно все тянуться
from .Picture.OCR import Picture_to_text as PTT #
from .Sound.Pooper import Sound_builder as SB #
import pathlib #
from django.http import Http404
from django.shortcuts import render
from .forms import History_File_Image_Voice

# Create your views here.
# взято с https://proglib.io/p/bezopasnaya-zagruzka-izobrazheniy-v-veb-prilozhenii-na-django-2020-05-26

from django.http import HttpResponse



# домашняя страница
def Poop_home(request):
    return render(request, 'Home_Page.html')

# Страница авторизации
def Poop_authorization(request):
	return HttpResponse("Здесь будет страница авторизации на сервисе Пуп.")

# Страница регистрации
def Poop_registration(request):
	return HttpResponse("Здесь будет страница регистрации на сервисе Пуп.")

# Страница хранилища
def Poop_storage(request):
	return HttpResponse("Здесь будет страница хранилища записей клиента на сервисе Пуп.")

# страница конвертации - создания новой записи
def user_history(request):
	# Обработка изображений, загруженных пользователем
	if request.method == 'POST':
		form = History_File_Image_Voice(request.POST, request.FILES)
		if form.is_valid(): # форма прошла валидацию
			form.save()
			# Получить текущий экземпляр объекта для отображения в шаблоне 
			img_obj = form.instance


			# Initialize working directory
			Working_directory = str(pathlib.Path(__file__).parent.absolute())

        	# Get path to picture loaded by user
			Path_to_picture = img_obj.History_File.path
        
        	# Get text from the picture and write it to the file.
        	# Return filename where text from the picture.
			Text_file_name = PTT().Get_text_from_picture(Path_to_picture)
        
        	# Get the path to file where text from picture
			Path_to_text_file = Working_directory +'\\'+ Text_file_name
        
        	# Start building PooP
        	# As output: a path to sound file with generated PooP
			Sound_file_name = SB().Build_Output_Sound(Working_directory, Path_to_text_file)
        
			voice_obj = form.instance

        	# Get the path to file where sound from picture
			voice_obj = Working_directory +'\\'+ Sound_file_name

			
			#voice_obj = form.instance
			#voice_obj = TEST_RUNNER.Main.I_Do_Somthing(img_obj)
			
			return render(request, 'New_History.html',  {'form': form, 'img_obj': img_obj, 'voice_obj':voice_obj})
	else:
		form = History_File_Image_Voice()
	return render(request, 'New_History.html', {'form': form})

# Страница просмотра старой записи
def History(request, user_history_id):
		try:
			voices = User_History.objects.get(pk=user_history_id)
		except User_History.DoesNotExist:
			raise Http404("User History does not exist")
		return render(request, 'History_Page.html', {'voices': voices})
	#return HttpResponse("Здесь будет страница со старой записью клиента на сервисе Пуп.")

# Страница с личными данными клиента
def Personal_page(request):
	return HttpResponse("Здесь будет страница с личными данными клиента сервиса Пуп.")
