from django.urls import re_path, path,include
from . import views

urlpatterns=[
    re_path('signup/',views.signup,name = 'signup'),
   path('account/', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
    path('search/', views.search_profile, name='search'),
    # path('profile/<username>/', views.profile, name='profile'),
    # path('user_profile/<username>/', views.user_profile, name='user_profile'),
]