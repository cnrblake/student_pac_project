from django.shortcuts import render, redirect
from .models import StudentTable
from .forms import StudentForm

# Create your views here.

def home_view(request):
    students = StudentTable.objects.all()
    context = {'students': students}
    return render(request, 'studentpac/home.html', context)

def add_student_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm()

    context = {'form': form}
    return render(request, 'studentpac/add_student.html', context)



