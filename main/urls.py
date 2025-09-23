from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('analytics/', views.analytics_dashboard, name='analytics'),
    path('api/responses/', views.api_responses, name='api_responses'),
    path('export/csv/', views.export_csv, name='export_csv'),  # Add this line
]