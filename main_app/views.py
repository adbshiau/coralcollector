from typing import List
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Coral, Location
from .forms import NoteForm

class CoralCreate(CreateView):
  model = Coral
  fields = '__all__'

class CoralUpdate(UpdateView):
  model = Coral
  fields = ['scientific_name', 'coral_type', 'difficulty', 'lighting', 'water_flow']

class CoralDelete(DeleteView):
  model = Coral
  success_url = '/corals/'

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

def corals_detail(request, coral_id):
  coral = Coral.objects.get(id=coral_id)
  unused_locations = Location.objects.exclude(id__in = coral.locations.all().values_list('id'))
  note_form = NoteForm()
  return render(request, 'corals/detail.html', {
    'coral': coral, 'note_form': note_form,
    'locations': unused_locations
  })

def add_note(request, coral_id):
  form = NoteForm(request.POST)
  # validate the form
  if form.is_valid():
    new_note = form.save(commit=False)
    new_note.coral_id = coral_id
    new_note.save()
  return redirect('detail', coral_id=coral_id)

def assoc_location(request, coral_id, location_id):
  Coral.objects.get(id=coral_id).locations.add(location_id)
  return redirect('detail', coral_id=coral_id)