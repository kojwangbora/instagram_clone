from django.urls import re_path, path,include
from . import views

urlpatterns=[
    re_path('signup/',views.signup,name = 'signup'),
   path('account/', include('django.contrib.auth.urls')),
    path('', views.index, name='index')
]