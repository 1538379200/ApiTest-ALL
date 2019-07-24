"""apitest URL Configuration

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
from django.urls import path
from userpage import views
urlpatterns = [
    path("testing",views.APITest,name="api"),
    path("logout",views.loginout,name="loginout"),
    path("",views.index,name="index"),
    path('loginpage',views.loginpage,name='loginpage'),
    path('login',views.userlogin,name="login"),
    path('usercheck',views.usercheck,name='usercheck'),
    path('sightin',views.sight,name='sightin'),
    path('sighting',views.sightpage,name='sighting'),
    path('admin/', admin.site.urls),
]
