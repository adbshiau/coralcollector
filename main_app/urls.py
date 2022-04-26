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
]