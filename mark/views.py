from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from student.models import StudentDetails 
from .models import MarkList
from .forms import EntryMarklistForm, UpdateMarklistForm


# Create your views here.
def options(request):
    return render(request, 'options.html')

# def insertMark(request):
#     student_data = StudentDetails.objects.all()

#     if request.method == "POST":
#         studentId = request.POST['studentname']
#         english = request.POST['english']
#         mal = request.POST['mal']
#         cs = request.POST['cs']
#         maths = request.POST['maths']
#         hindi = request.POST['hindi']

#         insert = MarkList(sub1=english,sub2=mal,sub3=cs,sub4=maths,sub5=hindi,student_id_id=studentId)

#         insert.save()

#         return redirect('insertMark')

#     return render(request, 'insert_marklist.html', {'student_data':student_data})

def insertMark(request):
    if request.method == 'POST':
        form = EntryMarklistForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('true')

    else:
        form = EntryMarklistForm()
    
    return render(request, 'insert_marklist.html', {'form':form})


def displayRecord(request):
    # student_with_mark = MarkList.objects.select_related('student_id')
    student_with_mark = MarkList.objects.filter(is_deleted=False)
    
    return render(request, 'displayRecord.html', {'student_with_mark': student_with_mark})


def oneRow(request):
    id = request.GET.get("uid")

    student_with_mark = get_object_or_404(
        MarkList.objects.select_related('student_id'), student_id=id
        )

    print(student_with_mark.student_id.name)
    print(student_with_mark.sub1)

    total = student_with_mark.sub1 + student_with_mark.sub2 + student_with_mark.sub3 +student_with_mark.sub4 +student_with_mark.sub5

    grade = gradeFinder(total)

    return render(request, 'oneRow.html', {
        'student_with_mark':student_with_mark,
        'total':total,
        'grade':grade
        })


def gradeFinder(total):
    if total >= 400:
        grade = 'A'
    elif total >= 300:
        grade = 'B'
    elif total >= 200:
        grade = 'C'
    else:
        grade = 'D'

    return grade

def updateMark(request, pk):
    marklist = get_object_or_404(MarkList, student_id=pk)

    if request.method == 'POST':
        form = UpdateMarklistForm(request.POST, instance=marklist)
        if form.is_valid():
            form.save()
            return redirect('displayRecord')
        else:
            print(form.errors)
    else:
        form = UpdateMarklistForm(instance=marklist)
    return render(request, 'updateMarklist.html', {'form':form, 'data':pk})


def delectRow(request, pk):
    student = get_object_or_404(StudentDetails, id=pk)

    student.is_deleted = True
    student.save()

    # Mark all corresponding MarkList records as deleted
    MarkList.objects.filter(student_id=pk).update(is_deleted=True)

    return redirect('displayRecord')