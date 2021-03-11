"""textutils URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf.urls import include
from django.views.generic import TemplateView 

urlpatterns = [
    path('google', TemplateView.as_view(template_name="social_app/index.html"),name='google_login'),
    path('admin/', admin.site.urls),
    
    path('',views.index, name='index'),
	path('analyze',views.analyze,name='analyze'),
	path('newlineremover',views.analyze,name='newlineremover'),
	path('extraspaceremover',views.analyze,name='extraspaceremover'),
	path('capslk',views.analyze,name='capslk'),
	path('removepunctuation',views.analyze,name='removepunc'),
	path('charcount',views.analyze,name='charcount'),
    path('accounts/', include('allauth.urls')), 

    
    
    path('users/',include('django.contrib.auth.urls')),
    path('users/',include('users.urls')),
    #path('profile/',user_views.profile,name='profile'),
    #path('password-reset/',auth_views.PasswordResetView.as_view(template_name=
    #    'registration/password_reset.html'),
     #   name='password_reset'),
    #path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name=
     #   'registration/password_reset_done.html'),
      #  name='password_reset_done'),
    #path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name=
     #   'registration/password_reset_confirm.html'),
      #  name='password_reset_confirm'),
    #path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name=
     #   'registration/password_reset_complete.html'),
      #  name='password_reset_complete'),

    


]
