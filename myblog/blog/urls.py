#-*-coding:utf-8_*_
#作者      :71460
#创建时间  :2019/3/15 15:18
#文件      :urls.py.py
#IDE       :PyCharm

from django.urls import path,include
from . import views
app_name = 'blog'
urlpatterns = [
    path('index/', views.index),
    path('article_page/<int:article_id>/', views.article_page ,name='article_page'),
    path('edit/<int:article_id>/', views.edit_page,name='edit_page'),
    path('edit_action/', views.edit_action,name='edit_action'),
]
