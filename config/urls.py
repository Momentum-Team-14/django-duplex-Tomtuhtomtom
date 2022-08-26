"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

# Main URLS file for directories right after the 127.0.0.1 server url
# use urlpatterns to create paths for those directories

# pretty much always need this line
from django.contrib import admin
# needed to use for urlpatterns
from django.urls import path, include
# I believe this is for opening whatever url you want from the runserver - need to find out
from django.views.generic import RedirectView
# needed to talk to your views.py in the app directory
from flashcards import views
# need both lines to access static in the settings
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.default.urls')),
]

urlpatterns += [
    path('flashcards/', include('flashcards.urls')),
]

urlpatterns += [
    path('', RedirectView.as_view(url='flashcards', permanent=False)),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)