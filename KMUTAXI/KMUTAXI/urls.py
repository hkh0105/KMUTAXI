from django.contrib import admin
from django.urls import path,include
<<<<<<< HEAD

=======
import account.views
>>>>>>> 41c1c0d276a31b76b9a7456b05826855449c54e2

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('mockdong/',include("mockdong.urls")),
=======
    path('',account.views.home, name = "home"),
    path('account/register', account.views.register_view,name="register"),
    path('account/login', account.views.login_view,name="login"),
    path('account/logout', account.views.logout_view,name="logout"),

>>>>>>> 41c1c0d276a31b76b9a7456b05826855449c54e2
]
