from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# class UserRegistrationForm(UserCreationForm):
#     email=forms.EmailField()
#     class Meta:
#         model=User
#         fields=['username','email','password1','password2']

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields=['username','password1','password2']

class NewRegister(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'password1','password2']
        
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Nombre de usuario'
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].label = 'Ingrese nuevamente contraseña'
        