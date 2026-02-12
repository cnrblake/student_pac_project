from django.shortcuts import render
from .models import PacTable

# Create your views here.

def home_view(request):
    pactable = PacTable.objects.all()
    context = {'pactable': pactable}
    return render(request, 'studentpac/home.html', context)



