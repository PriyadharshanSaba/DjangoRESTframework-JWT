from django.contrib import admin
from django.conf.urls import url, re_path
from bankapi import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    url(r'^api/token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^api/token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^hello/$', views.HelloView.as_view(), name='hello'),
    url(r'', views.fyleAPI.as_view ()),
    url(r'^hello/$', views.HelloView.as_view(), name='hello'),
    url(r'^admin/', admin.site.urls),

]

urlpatterns = format_suffix_patterns (urlpatterns)
