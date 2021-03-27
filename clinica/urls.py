from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('register', views.register, name='register'),
    path('browse', views.browse, name='browse'),
    path('buy', views.buy, name='buy'),
    path('buy/confirm_purchase', views.confirm_purchase, name='confirm_purchase')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
