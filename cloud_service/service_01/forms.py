from django import forms
from .models import User_History

class History_File_Image(forms.ModelForm):
	class Meta:
		model = User_History
		fields = ('User', 'History_File')
# Должна быть форма с полем image


#class LoginForm(forms.Form):
#    username = forms.CharField()
#    password = forms.CharField(widget=forms.PasswordInput)