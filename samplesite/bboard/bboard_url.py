from django.urls import path
from . import views

app_name = 'bboard'
urlpatterns = [
    path('<int:rubric_id>/', views.by_rubric, name='rubric'),
    path('add', views.BdcreateView.as_view(), name='add'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name  = 'logout'),
    path('sign_up/', views.sign_up, name = 'sign_up'),
    path('', views.index, name='index'),

]
