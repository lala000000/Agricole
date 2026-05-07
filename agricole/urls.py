from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('cultures/', views.cultures, name='cultures'),
    path('culture/new/', views.create_culture, name='create_culture'),
    path('culture/<int:id>/', views.culture, name='culture'),
    path('culture/<int:id>/edit/', views.edit_culture, name='edit_culture'),
    path('culture/<int:id>/delete/', views.delete_culture, name='delete_culture'),
    path('alertes/', views.alertes, name='alertes'),
    path('alertes/<int:id>/toggle/', views.toggle_alerte, name='toggle_alerte'),
    path('alertes/mark-all-read/', views.mark_all_alerts_read, name='mark_all_alerts_read'),
    path('observations/', views.observations, name='observations'),
    path('observations/add/', views.add_observation, name='add_observation'),
    path('parcel/new/', views.create_parcelle, name='create_parcelle'),
    path('parcel/<int:id>/', views.parcel, name='parcel'),
    path('parcel/<int:id>/edit/', views.edit_parcelle, name='edit_parcelle'),
    path('parcel/<int:id>/delete/', views.delete_parcelle, name='delete_parcelle'),
    path('parcels/', views.parcels, name='parcels'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('settings/', views.settings, name='settings'),
]