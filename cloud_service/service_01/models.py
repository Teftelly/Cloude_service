from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class User_History(models.Model):
	User = models.ForeignKey(
		User,
		on_delete = models.CASCADE
	)
	History_File = models.ImageField(
		'Изображение для чтения текста',

		# If True, the field is allowed to be blank. Default is False.

		blank = True,

		# upload_to - Этот атрибут обеспечивает способ установки каталога 
		# загрузки и имени файла. 
		# файл будет сохранен в MEDIA_ROOT / History_Files / YYYY/MM/DD

		upload_to = 'History_Files/%Y/%m/%d/'
	)
	History_Voice = models.FileField(
		'Аудиофайл пользователя для прослушивания',
		blank = True,
		upload_to = 'History_Voices/'
	)

	def get_absolute_url(self):
		return reverse('history', kwargs={'user_history_id': self.pk})