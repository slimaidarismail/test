from django.contrib import admin
from django.urls import path
from globalpages.views import HomePage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view(), name="home-page")
]
