from django.urls import path

from . import views

app_name = 'jitterbunk'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>/', views.personal, name='personal'),
    path('bunk/', views.sendbunk, name='sendbunk'),
    path('bunk/post', views.postbunk, name='postbunk'),
    path('users/<str:query>', views.getUsers, name='getUsers'),
]