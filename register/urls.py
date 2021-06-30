from django.urls import path

from . import views
urlpatterns = [


    path('', views.profile_view, name='profile'),
    path('registration/', views.register_view, name='reg'),
    path('auth/', views.auth_view, name='auth'),
    path('main/', views.mainpage_view, name='main'),
    path('pagination/', views.pagination_view, name='pagination_p'),
    path('newlink/', views.newgetlink_view, name='nLink'),
    path('^$/<str:link_slug>', views.home_view, name='goLink'),
    path('delete/<slug>', views.DelView.as_view(), name='delete')

]
