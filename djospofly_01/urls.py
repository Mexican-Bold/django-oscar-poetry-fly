"""
URL configuration for djospofly_01 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.apps import apps
from django.contrib import admin
from django.urls import include, path

from djospofly_01.spa.views import SpaView  # <-- here


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", SpaView.as_view(), name="spa"),  # <-- here
    path('', include(apps.get_app_config('oscar').urls[0])),


]

    #path('i18n/', include('django.conf.urls.i18n')),

    # The Django admin is not officially supported; expect breakage.
    # Nonetheless, it's often useful for debugging.

