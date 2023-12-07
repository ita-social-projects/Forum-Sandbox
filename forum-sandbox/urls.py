"""Forum URL Configuration

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
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from .views import MainPageView

urlpatterns = [
    path('api/main_page/', MainPageView.as_view(), name='main_page'),
    # path("admin/", admin.site.urls),
    path("", include("authentication.urls")),
    # path("api/", include("profiles.urls", namespace="profiles")),
    # path(
    #     "api/admin/",
    #     include("administration.urls", namespace="administration"),
    # ),
    # path("api/", include("search.urls", namespace="search")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


