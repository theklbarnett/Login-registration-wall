from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.render_wall),
    path('post_message', views.post_message),
    path('post_comment', views.post_comment),
    path('ajax/delete_post', views.delete_post)
]