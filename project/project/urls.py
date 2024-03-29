from django.contrib import admin
from django.urls import path, include
from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view()),
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('products/', include('simpleapp.urls')),  # делаем так, чтобы все адреса из нашего приложения (simpleapp/urls.py) сами автоматически подключались, когда мы их добавим.
    path('news/', include('news.urls')),
    path('sign/', include('sign.urls')),
    path('accounts/', include('allauth.urls')),
]