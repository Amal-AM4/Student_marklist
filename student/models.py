from django.db import models

# Create your models here.
class StudentDetails(models.Model):
    admin_no = models.CharField(max_length=8, blank=True, null=True, editable=False)
    name = models.CharField(max_length=30)
    phone_no = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    address = models.TextField()
    gender = models.CharField(max_length=3)
    dob = models.DateField(auto_now=False, auto_now_add=False)

    # Add a new field
    is_deleted = models.BooleanField(default=False)

    
    class Meta:
        db_table = 'StudentDetails'

    
    def __str__(self):
        return str(self.name)

