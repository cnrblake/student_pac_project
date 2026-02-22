from django.shortcuts import render, redirect
from .models import StudentTable, PacTable
from .forms import StudentForm, PacForm

# Create your views here.


def home_view(request):
    return render(request, 'studentpac/home.html')


def student_view(request):
    students = StudentTable.objects.all()
    context = {'students': students}
    return render(request, 'studentpac/student.html', context)

def add_student_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_view')
    else:
        form = StudentForm()

    context = {'form': form}
    return render(request, 'studentpac/add_student.html', context)

def pac_view(request):
    pacs = PacTable.objects.all()
    context = {'pacs': pacs}
    return render(request, 'studentpac/pac.html', context)

def add_pac_view(request):
    if request.method == 'POST':
        form = PacForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pac_view')
    else:
        form = PacForm()
    context = {'form': form}
    return render(request, 'studentpac/add_PAC.html', context)

def assigned_studnets_to_Pac(request):
    pacs = PacTable.objects.prefetch_related('studenttable_set').all()
    return render(request, 'pac_student.html', {'pacs': pacs})
