from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User_History(models)
	history_file = models.FileField(
        'файл исстории',
        blank=True,
        upload_to='history_files'
        )