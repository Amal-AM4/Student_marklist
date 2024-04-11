from django.shortcuts import render, HttpResponse, redirect
from .forms import StudentDetailsForms
from .models import StudentDetails



# Create your views here.
def insertStudent(request):
    if request.method == "POST":
        form = StudentDetailsForms(request.POST)
        if form.is_valid():

            name=form.cleaned_data['name']
            phone_no=form.cleaned_data['phone_no']
            email=form.cleaned_data['email']
            address=form.cleaned_data['address']
            gender=form.cleaned_data['gender']
            dob=form.cleaned_data['dob']
            
            student = StudentDetails(
                name=name,
                phone_no=phone_no,
                email=email,
                address=address,
                gender=gender,
                dob=dob
            )
            student.save()
            print(student)
            
            # return HttpResponse('sucessfull')
            return redirect('singleRow', student_id=student.id)
            
    else:
        form = StudentDetailsForms()
        return render(request, 'insert.html', {'form':form})
    

def singleRow(request, student_id):
    student = StudentDetails.objects.get(id=student_id)
    return render(request, 'singledata.html', {'student': student})
