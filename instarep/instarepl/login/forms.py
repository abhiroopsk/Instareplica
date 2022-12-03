from django import forms
from .models import Post
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name= forms.CharField(max_length=100)
    
    class Meta:
        
        model = User
        fields= [  'username','first_name',"last_name","email","password1","password2" ]

        # widgets ={
        #     'first_name' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Enter title'}),
        #     'lastname' : forms.TextInput(attrs={'class' : 'form-control'}),

        #     'email' : forms.EmailInput(attrs={'class' : 'form-control'}),
        # }

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args,**kwargs)

        self.fields['username'].widget.attrs['class']= 'form-control'
        self.fields['first_name'].widget.attrs['class']= 'form-control'
        self.fields['last_name'].widget.attrs['class']= 'form-control'
        self.fields['email'].widget.attrs['class']= 'form-control'
        self.fields['password1'].widget.attrs['class']= 'form-control'
        self.fields['password2'].widget.attrs['class']= 'form-control'

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'body','header_image')

        widgets= {
            'title' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Enter title'}),
            'author' : forms.Select(attrs={'class' : 'form-control',}),
            'body' : forms.Textarea(attrs={'class' : 'form-control','placeholder' : 'Enter description'}),

        }
class EditProfileForm(UserChangeForm):
    
    username= forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': ' form-control'}))
    first_name= forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': ' form-control'}))
    last_name= forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': ' form-control'}))
    email= forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'class': ' form-control'}))
    
    
    class Meta:
        
        model = User
        fields= [  'username','first_name',"last_name","email"]