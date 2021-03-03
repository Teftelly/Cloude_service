from django.contrib import admin

# Register your models here.

from .models import User_History, Test_Us_HF

admin.site.register(User_History)

admin.site.register(Test_Us_HF)