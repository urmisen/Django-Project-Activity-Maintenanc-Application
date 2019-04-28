from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.apps import apps

Profile=apps.get_model('project','Profile')
CT_Marks=apps.get_model('project','CT_Marks')
from django.contrib.auth import (
    authenticate,
    get_user_model

)

User = get_user_model()


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','teacher_id','department','hometown','address','dob','blood_group','institute']

class CT_MarksForm(forms.ModelForm):
    student_id = forms.IntegerField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    subject_name = forms.CharField()
    CT_1 = forms.IntegerField()
    CT_2 = forms.IntegerField()
    CT_3 = forms.IntegerField()
    CT_4 = forms.IntegerField()

    class Meta:
        model = CT_Marks
        fields = ['student_id', 'first_name', 'last_name', 'subject_name','CT_1','CT_2','CT_3','CT_4']