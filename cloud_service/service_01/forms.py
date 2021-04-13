from django import forms
from .models import User_History
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm

class History_File_Image_Voice(forms.ModelForm):
	class Meta:
		model = User_History
		fields = ('History_File',)
		exclude = ['History_Voice', 'User' ]
# 'History_Voice'
#class History_Page_Image_Voice(forms.ModelForm):
#	class Meta:
#		model = User_History
#		fields = ('User', 'History_File', 'History_Voice')	

#class LoginForm(forms.Form):
#    username = forms.CharField()
#    password = forms.CharField(widget=forms.PasswordInput)
class RegistrationForm(forms.ModelForm):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		fields = ['username', 'password']
		model = User

class LoginForm(forms.ModelForm):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		fields = ['username', 'password']
		model = User