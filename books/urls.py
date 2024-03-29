"""books URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include, path
from lib import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/',views.myapp1, name='myapp'),
    path('content/<int:num>',views.content, name='content'),
    path('create/', views.create, name='create'),
    path('index/<int:num>/', views.index, name='index'),
    path('find', views.find, name='find'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('sumple', views.sumple, name='sumple'),
    path('edit/<int:num>', views.edit, name='edit'),
    path('login/', views.Login.as_view(), name='login')






]
