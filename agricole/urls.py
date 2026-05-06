from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('cultures/', views.cultures, name='cultures'),
    path('alertes/', views.alertes, name='alertes'),
    path('observations/', views.observations, name='observations'),
    path('parcel/<int:id>/', views.parcel, name='parcel'),
    path('parcels/', views.parcels, name='parcels'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
]