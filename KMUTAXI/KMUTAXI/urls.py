from django.contrib import admin
from django.urls import include,path
import account.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hong/',include('hong.urls')),
    path('kmu/', include("kmu.urls")),
    path('mockdong/',include("mockdong.urls")),
    path('',account.views.home, name = "home"),
    path('account/register/', account.views.register_view,name="register"),
    path('account/login/', account.views.login_view,name="login"),
    path('account/logout/', account.views.logout_view,name="logout"),
]
