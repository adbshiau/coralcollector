from django.shortcuts import render
from django.http import HttpResponse

# THIS IS JUST MOCKING SOME  DATA SINCE WE DONT HAVE MODELS YET
# When we have a model, the class Coral and corals list will be deleted
class Coral:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

corals = [
  Coral('Nobu', 'tabby', 'foul little demon', 3),
  Coral('Sumi', 'tortoise shell', 'diluted tortoise shell', 0),
  Coral('Biri', 'black tripod', '3 legged cat', 4)
]

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello!</h1>')

def about(request):
    return render(request, 'about.html')

def corals_index(request):
    return render(request, 'corals/index.html', {'corals': corals})