"""redhuman URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^accounts/login/', auth_views.LoginView.as_view(), name='login'),
    url(r'^admin/', include('massadmin.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^doc_templates/', include('doc_templates.urls')),
    url(r'^notifications/', include('django_nyt.urls')),
    url(r'^import1c/', include('import1c.urls', namespace='import1c')),
    url(r'^applicants/', include('applicants.urls')),
    url(r'^bot/', include('telegram_bot.urls')),
    url(r'^async_utils/', include('async_utils.urls')),
    url(r'^', include('the_redhuman_is.urls')),
    url(r'^', include('django_telegrambot.urls')),
    url(r'^', include('django.contrib.auth.urls')),

    #url(r'^accounts/logout/$', django.contrib.auth.views.logout_then_login, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    try:
        import debug_toolbar
        urlpatterns = [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
    except ImportError:
        pass
