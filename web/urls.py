from django.contrib import admin
from django.urls import path
from globalpages.views import HomePage
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view(), name="home-page")
]

urlpatterns += staticfiles_urlpatterns()