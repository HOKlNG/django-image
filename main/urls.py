from django.contrib import admin
from django.urls import path, include, re_path

from .views import index, MyPage

urlpatterns = [
    path('',index),
    path('lotto',MyPage.as_view(template_name='number_recommand.html'))

]