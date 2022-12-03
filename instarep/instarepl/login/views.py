from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView,DetailView,CreateView
from .models import Post,User
from .models import Profile
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from . forms import SignUpForm,PostForm,EditProfileForm
from django.urls import reverse_lazy,reverse
from django.views import generic


# Create your views here.  

def follow(request):
    users= User.objects.all()
    print(users)
    return render(request,'registration/homepage.html',{'users':users})


def like_post(request):
    post= Post.objects.get(id= request.POST["post_id"])
    user= request.user
    post.likes.add(user)
    return redirect('home')

def unlike_post(request):
    post= Post.objects.get(id= request.POST["post_id"])
    user= request.user
    post.unlikes.add(user)
    return redirect('home')


class ShowProfilePageView(ListView):
    model= Profile
    model = Post
    template_name = 'registration/user_profile.html'
    

        
class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'register/registerpage.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


def HomeView(request):
    posts=Post.objects.all().order_by('-post_date')
    users= User.objects.all()
    return render(request,'registration/homepage.html',{'users':users,'posts':posts})

class AddPostView(CreateView):
    model= Post
    form_class= PostForm
    template_name = 'add_post.html'



