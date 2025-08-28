from django.urls import path
from . import views

urlpatterns = [
    path('coordinator/', views.coordinator_dashboard, name='coordinator_dashboard'),
    path('team/<int:team_id>/', views.team_dashboard, name='team_dashboard'),
    path('panelist/', views.panelist_dashboard, name='panelist_dashboard'),
    path('home/', views.home, name='home')
]
