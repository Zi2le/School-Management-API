from django.db import models

# Create your models here.
GENDER_CHOICE = (
    ('F', 'Female'),
    ('M', 'Male')
)
class Course(models.Model):
    name = models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    duration = models.CharField(max_length=100)   
    price = models.DecimalField(max_digits=12, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField(default=None)  

    def __str__(self):
        return self.name
    

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    gender= models.CharField(max_length=2, choices=GENDER_CHOICE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=None)
    

    def __str__(self):
        return self.name
    
# GENDER_CHOICE = (
#     ('F', 'Female'),
#     ('M', 'Male')
# )

class Student(models.Model):
     first_name = models.CharField(max_length=100)
     last_name = models.CharField(max_length=100)
     teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, blank=True, null=True)
     Age= models.PositiveIntegerField()
     gender= models.CharField(max_length=2, choices=GENDER_CHOICE)
     email = models.EmailField()
     address = models.CharField(max_length=100)
     


     def __str__(self):
        return self.name






class Admission(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    is_paid= models.BooleanField(default=False)    
    
    def __str__(self):
        return f"{self.student.names} registered"
