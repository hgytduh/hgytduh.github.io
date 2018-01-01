from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from members.models import Member


class RegistrationForm(ModelForm):
    username = forms.CharField(label=(u'Username'))
    email = forms.EmailField(label=(u'Email Address'))
    ign = forms.CharField(label=(u'IGN'))
    password = forms.CharField(
        label=(u'Password'), widget=forms.PasswordInput(render_value=False))

    class Meta:
        model = Member
        exclude = ('user',)

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(
            "That username is already taken, please select another.")

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError(
            "That email is already taken, please enter another or log in.")
    
    def clean_ign(self):
        ign = self.cleaned_data["ign"]
        try:
            Member.objects.get(ign=ign)
        except User.DoesNotExist:
            return ign
        raise forms.ValidationError(
            "That ign is already taken, please enter another or log in.")



class LoginForm(forms.Form):
    username = forms.CharField(label=(u'Username'))
    password = forms.CharField(
        label=(u'Password'), widget=forms.PasswordInput(render_value=False))

class NewPasswordForm(forms.Form):
    password = forms.CharField(label=(u'Password'))