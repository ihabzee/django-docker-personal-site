"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import include,path
from django.conf.urls import handler404
from base.admin import MyAdminSite, site
from article.api import ArticleViewSet
from resume.api import SectionViewSet
from contact.api import ContactViewSet
from rest_framework import routers
from django.views.generic import RedirectView

admin.site.__class__ = MyAdminSite
 

from . import views
router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'sections', SectionViewSet)
router.register(r'contact-me', ContactViewSet)
# handler404 = 'base.views.handler404'
 
urlpatterns = [
    # path('', include('article.urls')),
    path('contact/', RedirectView.as_view(url='/contact-me')),
    path('articles/', RedirectView.as_view(url='/articles')),
    path('resume/', RedirectView.as_view(url='/resume')),
    path('', include('vue_app.urls')), 
    path('contact-me', include('vue_app.urls')),
    path('resume', include('vue_app.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]


# for serving static files
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 