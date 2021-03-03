from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class User_History(models.Model):
	User = models.ForeignKey(
		User,
		on_delete = models.CASCADE
	)
	History_File = models.ImageField(
		'Файл истории пользователя',

		# If True, the field is allowed to be blank. Default is False.

		blank = True,

		# upload_to - Этот атрибут обеспечивает способ установки каталога 
		# загрузки и имени файла. 
		# файл будет сохранен в MEDIA_ROOT / History_Files / YYYY/MM/DD

		upload_to = 'History_Files/%Y/%m/%d/'
	)

class Test_Us_HF(models.Model):
	text = models.CharField(max_length = 120)