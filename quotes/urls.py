from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.login_user, name="login"),
    path('', views.home, name="home"),
    path('about.html', views.about, name="about"),
    path('news.html', views.news, name="news"),
    path('add_stock.html', views.add_stock, name="add_stock"),
    path('delete/<stock_id>', views.delete, name="delete"),
    path('delete_stock.html', views.delete_stock, name="delete_stock"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),
    path('edit_profile.html', views.edit_profile, name='edit_profile'),
    path('change_password.html', views.change_password, name='change_password'),
]