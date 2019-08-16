"""logger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.utils.translation import gettext_lazy as _

from entry.urls import urlpatterns as entry_urlpatterns

admin.site.site_header = _('Happy logger')
admin.site.index_title = _('Be happy and log everything')
admin.site.site_title = _('Life is joy')

urlpatterns = [
    path('', include(entry_urlpatterns)),
    path('admin/', admin.site.urls),
]
