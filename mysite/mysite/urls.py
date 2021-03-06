"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

import imp
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),

    path('admin/', admin.site.urls),
    path('info', views.info),

    path('get/all', views.get_all_cve),
    path('get/new', views.get_new_cve),
    path('get/critical', views.get_critical_cve),
    path('get/query/', views.get_by_query_cve),


    path('get/pdf/all', views.get_all_pdf_cve),
    path('get/pdf/new', views.get_new_pdf),
    path('get/pdf/critical', views.get_pdf_critical_cve)
    
    # path('get/pdf/new') 
]
