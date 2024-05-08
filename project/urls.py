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
    path('api/payment/', include("payments.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)