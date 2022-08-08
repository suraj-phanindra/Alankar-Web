from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Student_new(models.Model):
    Gender_choice = (('M', 'Male'), ('F', 'Female'), ('O', 'Other'))
    School_category = (('G', 'Government'), ('P', 'Private'))
    Medium_choice = (('E', 'English'), ('H', 'Hindi'), ('O', 'Other'))
    Volunteer = models.ForeignObject
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    fathers_name = models.CharField(max_length=50)
    mothers_name = models.CharField(max_length=50)
    Gender = models.CharField(max_length=1, choices=Gender_choice)
    students_aadhar_number = models.IntegerField()
    contact_number = PhoneNumberField(blank=False)
    dob = models.DateField()
    Address = models.CharField(max_length=300)
    doj = models.DateField()
    id_card = models.ImageField(upload_to='photos/%Y/%m/%d/')
    standard = models.IntegerField(default=0,blank=True)
    School_name = models.CharField(max_length=200, blank=True, default='None')
    school_category = models.CharField(max_length=1, choices=School_category, default='G')
    Medium = models.CharField(max_length=1, choices=Medium_choice, default='Hindi')
    Signature = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.first_name


class Volunteer_new(models.Model):
    Gender_choice = (('M', 'Male'), ('F', 'Female'), ('O', 'Other'))
    preferred_choice = (('S45', 'Sector 45'), ('S15', 'Sector 15 part 2'), ('S14', 'Sector 14'))
    Volunteer_id = models.IntegerField()
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    mobile_number = PhoneNumberField(blank=False)
    email_address = models.EmailField(blank=False)
    Gender = models.CharField(max_length=1, choices=Gender_choice)
    doj = models.DateField()
    preferred_Centre = models.CharField(max_length=3, choices=preferred_choice)
    id_card = models.ImageField(upload_to='photos/%Y/%m/%d/')
    student_enrolled = models.ManyToManyField(Student_new, blank=True)

    def __str__(self):
        return self.first_name


