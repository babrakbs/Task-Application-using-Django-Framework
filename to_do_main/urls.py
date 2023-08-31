from django.contrib import admin
from django.urls import path, include
from to_do_main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('update-task/<id>', views.update_task),
    path('delete-task/<id>', views.delete_task),
]
