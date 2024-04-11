from django import forms
from .models import StudentDetails

class StudentDetailsForms(forms.ModelForm):
    name = forms.CharField(
        label='Student Name',
        max_length= 10,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Enter a name', 'class': 'formname'})
        )
    
    phone_no = forms.CharField(required=False, max_length=10)
    
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])

    dob = forms.DateField()


    class Meta:
        model = StudentDetails
        fields = ['name', 'phone_no', 'email', 'address', 'gender', 'dob']
        exclude = ['admin_no']


# class FeedbackForm(forms.Form):
#     name = forms.CharField(
#         label='Phone Number',
#         max_length= 10,
#         required=False,
        
#         widget=forms.TextInput(attrs={'placeholder': '123-456-7890'})
#         )
    
#     age = forms.IntegerField(required=False)