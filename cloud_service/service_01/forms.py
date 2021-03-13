from django import forms
from .models import User_History

class History_File_Image_Voice(forms.ModelForm):
	class Meta:
		model = User_History
		fields = ('User', 'History_File', 'History_Voice')

#class History_Page_Image_Voice(forms.ModelForm):
#	class Meta:
#		model = User_History
#		fields = ('User', 'History_File', 'History_Voice')	

#class LoginForm(forms.Form):
#    username = forms.CharField()
#    password = forms.CharField(widget=forms.PasswordInput)