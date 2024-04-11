from django import forms
from student.models import StudentDetails
from .models import MarkList


class EntryMarklistForm (forms.ModelForm): 

    class Meta:
        model = MarkList  
        fields = '__all__'


class UpdateMarklistForm (forms.ModelForm): 

    class Meta:
        model = MarkList  
        exclude = ['student_id']

        