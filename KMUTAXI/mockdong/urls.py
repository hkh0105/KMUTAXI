from django.urls import path
from . import views

urlpatterns = [
    path('md_station/', views.md_station, name="md_station"),
    path('md_station/<int:mockdongboard_id>', views.detail, name ="md_detail"),
    path('md_station/new', views.new, name ="md_new"),
    path('md_station/create', views.create, name="md_create"),
    path('md_station/edit//<int:mockdongboard_id>', views.edit, name="md_edit"),
    path('md_station/update//<int:mockdongboard_id>', views.update, name="md_update"),
    path('md_station/delete//<int:mockdongboard_id>', views.delete, name="md_delete"),
]
    
