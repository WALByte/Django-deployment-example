from django.contrib import admin
from django.urls import re_path
from basicapp import views

urlpatterns = [
    re_path(r'^$',views.index, name="index"), 
    re_path(r'^formpage/',views.form_name_view, name="form_name_view"),
    re_path(r'^admin/', admin.site.urls ),  

]

