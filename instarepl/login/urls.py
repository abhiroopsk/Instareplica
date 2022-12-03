from django.urls import path
from .views import UserRegisterView,UserEditView,ShowProfilePageView
from . import views
from .views import HomeView,AddPostView  ,like_post,unlike_post,follow


urlpatterns = [

    path('register/', UserRegisterView.as_view(), name= 'register'),
    path('edit_profile/', UserEditView.as_view(), name= 'edit_profile'),
    path('',HomeView,name="home"),
    path('post/', AddPostView.as_view(), name="add_post"),
    path('profile/',ShowProfilePageView.as_view(), name='show_profile_page'),
    path('like/', like_post, name= 'like_post'), 
    path('unlike/', unlike_post, name= 'like_post'),    
       
]
