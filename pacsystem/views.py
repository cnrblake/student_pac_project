from django.shortcuts import render, redirect
from .models import StudentTable, PacTable
from .forms import StudentForm, PacForm

def home_view(request):
    return render(request, 'studentpac/home.html')

# show the student table
def student_view(request):
    # gets all rows in student table
    students = StudentTable.objects.all()
    # allows the rows to shown
    context = {'students': students}
    # allows the rows to be shown on a certain html page
    return render(request, 'studentpac/student.html', context)

# add a student
def add_student_view(request):
    if request.method == 'POST':
        # post to the student form
        form = StudentForm(request.POST)
        # if all fields are valid
        if form.is_valid():
            # save the fields to the table
            form.save()
            # redirects the user back to the student view page
            return redirect('student_view')
    else:
        form = StudentForm()

    # display add_student.html with the form
    context = {'form': form}
    return render(request, 'studentpac/add_student.html', context)


# update a students information
def update_student(request, f_oid):
    # what row is being edited
    obj = StudentTable.objects.get(StudentID=f_oid)
    form = StudentForm(instance=obj)
    if request.method == 'POST':
        # the student form
        form = StudentForm(request.POST, instance=obj)
        if form.is_valid():
            # save the changes
            form.save()
             # redirects the user back to the student view page
            return redirect('student_view')
    context = {'form': form}
    return render(request, 'studentpac/edit_student.html', context)

# delete a student
def delete_student(request, f_oid):
    obj = StudentTable.objects.get(StudentID=f_oid)
    if request.method == 'POST':
        obj.delete()
        return redirect('student_view')
    context = {'obj': obj}
    return render(request, 'studentpac/delete_student.html', context)

# get all students with the PAC ID of
def student_view_by_pac(request, f_oid):
    # filters by PAC ID
    obj = StudentTable.objects.get(PacID=f_oid)
    # returns only them
    context = {'students' : obj}
    return render(request, 'studentpac/pac_student.html',context)

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
def update_PAC(request, f_oid):
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
def delete_PAC(request, f_oid):
    obj = PacTable.objects.get(PacID=f_oid)
    if request.method == 'POST':
        obj.delete()
        return redirect('pac_view')
    context = {'obj': obj}
    return render(request, 'studentpac/delete_PAC.html', context)

def assigned_students_to_Pac(request):
    pacs = PacTable.objects.prefetch_related('studenttable_set').all()
    return render(request, 'studentpac/pac_student.html', {'pacs': pacs})
