"""pycontw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
#from django.conf.urls import include, url
#from django.contrib import admin

#urlpatterns = [
#    url(r'^admin/', include(admin.site.urls)),
#]

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.views.i18n import set_language

from crawler.views import crawler

urlpatterns = i18n_patterns(

    # Add top-level URL patterns here.
    url(r'^$', crawler, name='home'),
    url(r'^crawler/', include('crawler.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
)

urlpatterns += [
    url(r'^set-language/$', set_language, name='set_language'),
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

