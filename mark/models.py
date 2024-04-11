from django.db import models
from student.models import StudentDetails

# Create your models here.

class MarkList(models.Model):
    student_id = models.ForeignKey(StudentDetails, on_delete=models.CASCADE)
    sub1 = models.DecimalField(max_digits=5, decimal_places=2)
    sub2 = models.DecimalField(max_digits=5, decimal_places=2)
    sub3 = models.DecimalField(max_digits=5, decimal_places=2)
    sub4 = models.DecimalField(max_digits=5, decimal_places=2)
    sub5 = models.DecimalField(max_digits=5, decimal_places=2)

    # Add a new field
    is_deleted = models.BooleanField(default=False)


    class Meta:
        db_table = 'MarkList'

    # def __str__(self):
    #     return str(self.student_id.name)
