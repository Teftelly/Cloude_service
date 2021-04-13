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
from datetime import datetime


home_menu = 	[{'title': "Авторизация",		'url_name': 'author'},
				 {'title': "Регистрация",		'url_name': 'registr'}]
authoriz_menu = [{'title': "Главная страница",	'url_name': 'home'},
				 {'title': "Регистрация",		'url_name': 'registr'}]
registr_menu =	[{'title': "Главная страница",	'url_name': 'home'},
				 {'title': "Авторизация",		'url_name': 'author'}]
history_menu =	[{'title': "Личный кабинет",	'url_name': 'storage'},
				{'title': "Выход", 'url_name': 'home'}]
pers_menu =		[{'title': "Выход", 'url_name': 'home'}]

# домашняя страница
def Poop_home(request):
	context = {
		'menu': home_menu,
		'title': "ГЛАВНАЯ СТРАНИЦА"
	}
	return render(request, 'Home_Page.html', context=context)

# Страница авторизации
def Poop_authorization(request):
	context = {
		'menu':		authoriz_menu,
		'title':	"АВТОРИЗАЦИЯ"
	}
	return render(request, 'Authorization_Page.html', context=context)

# Страница регистрации
def Poop_registration(request):
	context = {
		'menu':		registr_menu,
		'title':	"РЕГИСТРАЦИЯ"
	}
	return render(request, 'Registration_Page.html', context=context)

# Страница хранилища и личного кабинета
def Poop_storage(request):
	posts = User_History.objects.all()
	context = {
		'posts':	posts,
		'menu':		pers_menu,
		'title':	"ЛИЧНЫЙ КАБИНЕТ"
	}
	return render(request, 'Storage_Page.html', context=context)

# страница конвертации - создания новой записи
def user_history(request):
	# Обработка изображений, загруженных пользователем
	if request.method == 'POST':
		form = History_File_Image_Voice(request.POST, request.FILES)

		if form.is_valid(): # форма прошла валидацию
			form.save()
			# Получить текущий экземпляр объекта для отображения в шаблоне 
			user_history = form.instance
			picture_obj = (user_history.History_File.path)
			Text_file_name = PTT().Get_text_from_picture(picture_obj)
			# переместить аудио файл в нужную папку
			Working_directory = pathlib.Path(__file__).parent.absolute().parent

			Sound_file_name = SB().Build_Output_Sound(str(Working_directory / 'service_01'), str(Working_directory / 'Output.txt'))
			curr_time = datetime.now()
			new_path = str(Working_directory/'media'/'History_Voices'/'Output_PooP_{day}_{minute}_{sec}.wav'\
				.format(day=curr_time.day, minute=curr_time.minute, sec=curr_time.second))
			shutil.move(str(Working_directory / 'Output_PooP.wav'), new_path)
			user_history.History_Voice = new_path
			user_history.save()
			# Словарь1
			context1 = {
				'menu':			history_menu,
				'title':		"НОВАЯ ПУП-ИСТОРИЯ",
				'form':			form,
				'img_obj':		user_history,
				'voice_obj':	user_history
			}
			return render(request, 'New_History.html',  context=context1)

	else:
		# Словарь2

		form = History_File_Image_Voice()

	return render(request, 'New_History.html', {
		'menu':		history_menu,
		'title':	"НОВАЯ ПУП-ИСТОРИЯ",
		'form':		form
	})

# Страница просмотра старой записи
def History(request, user_history_id):
		try:
			voices = User_History.objects.get(pk=user_history_id)
		except User_History.DoesNotExist:
			raise Http404("User History does not exist")
		context = {
			'menu':		history_menu,
			'title':	"АРХИВ ПУП-ИСТОРИЙ",
			'voices':	voices
		}
		return render(request, 'History_Page.html', context=context)
	#return HttpResponse("Здесь будет страница со старой записью клиента на сервисе Пуп.")
