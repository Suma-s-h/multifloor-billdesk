from django import forms
from django.contrib.auth.models import User
from learnapp.models import userDetails
from django_recaptcha.fields import ReCaptchaField

class userForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        #fields = "_all_"
        fields = ['username','email','password']

class userprofileForm(forms.ModelForm):
    class Meta:
        model = userDetails
        fields = ['phone','address','street','city','state','zipcode','img']
    captcha = ReCaptchaField()

class userupdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']


class userprofileupdateForm(forms.ModelForm):
    class Meta:
        model = userDetails
        fields = ['phone','address','street','city','state','zipcode','img']
