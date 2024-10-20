from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('', views.home, name='home'),

    # Bin Type URLs
    path('bin-types/', views.BinTypeListView.as_view(), name='bin_type_list'),
    path('bin-type/create/', views.BinTypeCreateView.as_view(), name='create_bin_type'),
    path('bin-type/<int:pk>/update/', views.BinTypeUpdateView.as_view(), name='update_bin_type'),
    path('bin-type/<int:pk>/delete/', views.BinTypeDeleteView.as_view(), name='delete_bin_type'),

    # Bin URLs
    path('bins/', views.BinListView.as_view(), name='bin_list'),
    path('bin/<int:pk>/', views.BinDetailView.as_view(), name='bin_detail'),
    path('bin/create/', views.BinCreateView.as_view(), name='create_bin'),
    path('bin/<int:pk>/update/', views.BinUpdateView.as_view(), name='update_bin'),
    path('bin/<int:pk>/delete/', views.BinDeleteView.as_view(), name='delete_bin'),

    # Collection URLs
    path('collections/', views.CollectionListView.as_view(), name='collection_list'),
    path('collection/create/', views.CollectionCreateView.as_view(), name='create_collection'),
    path('collection/<int:pk>/update/', views.CollectionUpdateView.as_view(), name='update_collection'),
    path('collection/<int:pk>/delete/', views.CollectionDeleteView.as_view(), name='delete_collection'),

    # Maintenance Log URLs
    path('maintenance-logs/', views.MaintenanceLogListView.as_view(), name='maintenance_log_list'),
    path('maintenance-log/create/', views.MaintenanceLogCreateView.as_view(), name='create_maintenance_log'),
    path('maintenance-log/<int:pk>/update/', views.MaintenanceLogUpdateView.as_view(), name='update_maintenance_log'),
    path('maintenance-log/<int:pk>/delete/', views.MaintenanceLogDeleteView.as_view(), name='delete_maintenance_log'),

    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),

    # Charts URLs
    path('bin_chart/', views.bin_chart, name='bin_chart'),
    path('collection_chart/', views.collection_chart, name='collection_chart'),
    path('maintenance_chart/', views.maintenance_chart, name='maintenance_chart'),
]
    

