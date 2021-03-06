"""blogapi URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from api.views import CustomAuthToken, Logout, Register

# Routers provide an easy way of automatically determining the URL conf.
from api.viewsets import CategoryViewSet, PostViewSet

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet, base_name="category")
router.register(r'posts', PostViewSet, base_name="post")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html")),
    path('api/v1/web-auth/', include('rest_framework.urls'), name="web-auth"),
    path('api/v1/login', CustomAuthToken.as_view(), name="login"),
    path('api/v1/register', Register.as_view(), name="register"),
    path('api/v1/', include(router.urls)),
    path('api/v1/logout/', Logout.as_view(), name="logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
