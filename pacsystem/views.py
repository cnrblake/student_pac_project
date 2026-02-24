from django.shortcuts import render, redirect
from .models import StudentTable, PacTable
from .forms import StudentForm, PacForm

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
            return redirect('student_view')  # redirects the user back to the student view page
    else:
        form = StudentForm()

    context = {'form': form}
    return render(request, 'studentpac/add_student.html', context)


# allows a student row to be modified
def updateStudent(request, f_oid):
    obj = StudentTable.objects.get(StudentID=f_oid)
    form = StudentForm(instance=obj)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('student_view') # redirects the user back to the student view page
    context = {'form': form}
    return render(request, 'studentpac/edit_student.html', context)

# allows a student row to be deleted
def deleteStudent(request, f_oid):
    obj = StudentTable.objects.get(StudentID=f_oid)
    if request.method == 'POST':
        obj.delete()
        return redirect('student_view')
    context = {'obj': obj}
    return render(request, 'studentpac/delete_student.html', context)


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

# allows a PAC row to be modified
def updatePAC(request, f_oid):
    obj = PacTable.objects.get(PacID=f_oid)
    form = PacForm(instance=obj)
    if request.method == 'POST':
        form = PacForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('pac_view') # redirects the user back to the pac view page
    context = {'form': form}
    return render(request, 'studentpac/edit_PAC.html', context)

# allows a PAC row to be deleted
def deletePAC(request, f_oid):
    obj = PacTable.objects.get(PacID=f_oid)
    if request.method == 'POST':
        obj.delete()
        return redirect('pac_view')
    context = {'obj': obj}
    return render(request, 'studentpac/delete_PAC.html', context)

def assigned_studnets_to_Pac(request):
    pacs = PacTable.objects.prefetch_related('studenttable_set').all()
    return render(request, 'pac_student.html', {'pacs': pacs})
