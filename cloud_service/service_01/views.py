from .models import User_History
from django.http import Http404
from django.shortcuts import render
from .forms import History_File_Image_Voice
from .Sound.Pooper import Sound_builder as SB
from .Picture.OCR import Picture_to_text as PTT
import pathlib
from django.http import HttpResponse
from django.core.files.base import File
import shutil
import os


# домашняя страница
def Poop_home(request):
    return HttpResponse("Здесь будет страница с описанием работы сервиса Пуп.")

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
		if form.is_valid():
			form.save()
			# Получить текущий экземпляр объекта для отображения в шаблоне 
			user_history = form.instance
			picture_obj = (user_history.History_File.path)
			Text_file_name = PTT().Get_text_from_picture(picture_obj)
			# переместить аудио файл в нужную папку
			working_directory = pathlib.Path(__file__).parent.absolute().parent
			print(working_directory)

			Sound_file_name = SB().Build_Output_Sound(str(working_directory / 'service_01'), str(working_directory / 'Output.txt'))
			try:
				os.remove(working_directory/'media'/'History_Voices'/'Output_PooP.wav')
			except FileNotFoundError:
				pass
			shutil.move(str(working_directory / 'Output_PooP.wav'), str(working_directory/'media'/'History_Voices'/'Output_PooP.wav'))
			user_history.History_Voice = str(working_directory/'media'/'History_Voices'/'Output_PooP.wav')
			user_history.save()
			user_history = User_History.objects.all().last()
			print('path  ', user_history.History_Voice.path)
			print('obj  ', user_history.History_Voice.path)

			
			return render(request, 'New_History.html',  {'form': form, 'history': user_history})
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
