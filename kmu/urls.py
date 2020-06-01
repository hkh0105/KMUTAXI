from django.urls import path
from .import views

urlpatterns = [
    path('kmu_station/', views.kmu_station, name="kmu_station"),
    path('<int:kmuboard_id>/', views.detail, name="kmu_detail"),
    path('new/', views.new, name="kmu_new"),
    path('create/', views.create, name="kmu_create"),
    path('edit/<int:kmuboard_id>',views.edit, name = "kmu_edit"),
    path('update/<int:kmuboard_id>',views.update, name = "kmu_update"),
    path('delete/<int:kmuboard_id>',views.delete, name = "kmu_delete"),
]
