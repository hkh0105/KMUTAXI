from django.contrib import admin
from django.urls import path,include
import account.views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',account.views.home, name = "home"),
    path('account/register', account.views.register_view,name="register"),
    path('account/login', account.views.login_view,name="login"),
    path('account/logout', account.views.logout_view,name="logout"),

]
