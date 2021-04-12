from django.urls import path

from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('<int:article_id>/leave_comment/', views.leave_comment, name='leave_comment'),
    path('dynamic', views.dynamic, name='dynamic'),
    path('dynamic/leave_comment_2/', views.leave_comment_2, name='leave_comment_2'),

]


