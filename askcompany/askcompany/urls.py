from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # 어떤 url이 오면 어떤 함수를 호출하겠다.
    path('shop/', include('shop.urls')),
    path('blog/', include('blog.urls')),
]
