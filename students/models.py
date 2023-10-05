from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    mother_Fname = models.CharField(max_length=50)
    mother_Lname = models.CharField(max_length=50)
    father_Fname = models.CharField(max_length=50)
    father_Lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    fee = models.FloatField()

    FEE_STATUS_CHOICES = [
        ('paid', 'Paid'),
        ('due', 'Due'),
        ('past', 'Past Due'),
    ]

    fee_status = models.CharField(max_length=10, choices=FEE_STATUS_CHOICES)

    STUDENT_STATUS_CHOICES = [
        ('current', 'Current Student'),
        ('past', 'Past Student'),
        ('sick', 'Sick Student'),
    ]

    student_status = models.CharField(max_length=10, choices=STUDENT_STATUS_CHOICES)
    allergies = models.CharField(max_length=255)

    def __str__(self):
        return f'Student: {self.first_name} {self.last_name}'


class Certification(models.Model):
    CERT_CHOICES = [
        ('first_aid', 'First Aid'),
        ('cpr', 'CPR'),
        ('6m_criminal_record', '6m Criminal Record'),
        ('1yr_criminal_record', '1yr Criminal Record'),
    ]

    name = models.CharField(max_length=50, choices=CERT_CHOICES)

    def __str__(self):
        return self.get_name_display()



class Staff(models.Model):
    staff_first_name = models.CharField(max_length=50)
    staff_last_name = models.CharField(max_length=50)
    staff_birth_date = models.DateField()
    staff_email = models.EmailField()
    staff_phone = models.CharField(max_length=15)
    

    CERTIFICATE_CHOICES = [
        ('first_aid', 'First Aid'),
        ('cpr', 'CPR'),
        ('6m_criminal_record', '6m Criminal Record'),
        ('1yr_criminal_record', '1yr Criminal Record'),
    ]
    certificates = models.ManyToManyField(Certification, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
