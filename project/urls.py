"""project URL Configuration

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
from django.urls import path, include
from django.http import HttpResponse
from django.utils.safestring import mark_safe

from project import settings
from django.conf.urls.static import static


def home(request):
    message = "Welcome to our pfa backend!<br><a href='/admin/'>go to admin</a><br><a href='api/auth/login/'>go to user</a>"
    content = f"<h3>{mark_safe(message)}</h3>"
    return HttpResponse(content)


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/auth/', include("account.urls")),
    path('api/products/', include("products.urls")),
    path('api/carts/', include("carts.urls")),
    path('api/orders/', include("orders.urls")),
    path('api/dash/', include("dashboard.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)