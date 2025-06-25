from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
     path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('report-lost/', views.report_lost, name='report_lost'),
    path('report-found/', views.report_found, name='report_found'),
    path('gallery/', views.gallery, name='gallery'),
    path('resolve-lost/<int:item_id>/', views.resolve_lost_item, name='resolve_lost'),
    path('resolve-found/<int:item_id>/', views.resolve_found_item, name='resolve_found'),
]
