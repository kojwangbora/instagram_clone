from django.urls import re_path, path,include
from . import views
from django.contrib.auth.views import LoginView
from insta.views import PostLikeToggle
# from django.contrib.auth import authenticate, login

urlpatterns=[
    re_path(r'index/', views.index, name='index'),
    re_path('welcome/',views.welcome,name='welcome'),
    re_path('signup',views.signup,name = 'signup'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('account/', include('django.contrib.auth.urls')),
    re_path(r'', LoginView.as_view(), {"next_page": '/'}),
    
    path('user_profile/<username>/', views.user_profile, name='user_profile'),
    
    path('profile/<username>/', views.profile, name='profile'),
   
    path('search/', views.search_profile, name='search'),
    path('post/<id>', views.post_comment, name='comment'),
    path('post/<id>/like', PostLikeToggle.as_view(), name='liked'),
    path('like', views.like_post, name='like_post'),
]