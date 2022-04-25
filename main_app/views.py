from django.shortcuts import render
from django.http import HttpResponse
from .models import Coral

# Create your views here.
def home(request):
  return HttpResponse('<h1>Hello!</h1>')

def about(request):
  return render(request, 'about.html')

def corals_index(request):
  corals = Coral.objects.all()
  return render(request, 'corals/index.html', {'corals': corals})

def corals_detail(request, coral_id):
  coral = Coral.objects.get(id=coral_id)
  return render(request, 'corals/detail.html', {'coral': coral})