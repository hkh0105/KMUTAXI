from django.urls import include,path
from . import views

urlpatterns = [
    path('',views.hong , name="hong_station"),
    path('<int:taxi_id>',views.detail,name ="hong_detail"),
    path('new',views.new,name="hong_new"),
    path('create',views.create,name="hong_create"),
    path('edit/<int:taxi_id>',views.edit,name="hong_edit"),
    path('update/<int:taxi_id>',views.update,name="hong_update"),
     path('delete/<int:texi_id>',views.delete, name = 'hong_delete'),
     path('<int:texi_id>/comment/create',views.comment_create, name = 'hong_comment_create'),
     path('comment/delete/<int:comment_id>',views.comment_delete, name = 'hong_comment_delete'),
]