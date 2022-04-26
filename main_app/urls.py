from django.urls import path
from corals.views import CoralList
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('corals/', views.corals_index, name='index'),
    path('corals/<int:coral_id>/', views.corals_detail, name='detail'),
    path('corals/', CoralList.as_view(), name='corals_index'),
]