from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('corals/', views.corals_index, name='index'),
    path('corals/<int:coral_id>/', views.corals_detail, name='detail'),
    path('corals/create/', views.CoralCreate.as_view(), name='corals_create'),
    path('corals/<int:pk>/update/', views.CoralUpdate.as_view(), name='corals_update'),
    path('corals/<int:pk>/delete/', views.CoralDelete.as_view(), name='corals_delete'),
    path('corals/<int:coral_id>/add_note/', views.add_note, name='add_note'),
    path('corals/<int:coral_id>/assoc_location/<int:location_id>/', views.assoc_location, name='assoc_location'),
    path('corals/<int:coral_id>/add_photo/', views.add_photo, name='add_photo'),
    path('locations/', views.LocationList.as_view(), name='locations_index'),
    path('locations/<int:pk>/', views.LocationDetail.as_view(), name='locations_detail'),
    path('locations/create/', views.LocationCreate.as_view(), name='locations_create'),
    path('locations/<int:pk>/update/', views.LocationUpdate.as_view(), name='locations_update'),
    path('locations/<int:pk>/delete/', views.LocationDelete.as_view(), name='locations_delete'),
]