

from django.urls import path,include
from . import views
urlpatterns = [

    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('about', views.about, name='about'),
    path('query',views.query, name = 'query'),
    path('delete_last_record/', views.query, name='delete_last_record')

]
