from django.urls import re_path, path,include
from . import views
from django.contrib.auth.views import LoginView
# from django.contrib.auth import authenticate, login

urlpatterns=[
    re_path(r'index/', views.index, name='index'),
    re_path('welcome/',views.welcome,name='welcome'),
    re_path('signup',views.signup,name = 'signup'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('account/', include('django.contrib.auth.urls')),
    re_path(r'', LoginView.as_view(), {"next_page": '/'}),
    
    path('profile/<username>/', views.profile, name='profile'),
    path('user_profile/<username>/', views.user_profile, name='user_profile'),
    path('search/', views.search_profile, name='search'),
]