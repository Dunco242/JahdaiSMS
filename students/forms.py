from django import forms
from .models import Student, Staff, Certification

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name', 'last_name', 'birth_date', 'mother_Fname', 'mother_Lname',
            'father_Fname', 'father_Lname', 'email', 'phone', 'fee', 'fee_status',
            'student_status', 'allergies'
        ]
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'birth_date': 'Birth Date',
            'mother_Fname': "Mother's First Name",
            'mother_Lname': "Mother's Last Name",
            'father_Fname': "Father's First Name",
            'father_Lname': "Father's Last Name",
            'email': 'Email',
            'phone': 'Phone',
            'fee': 'Fee',
            'fee_status': 'Fee Status',
            'student_status': 'Student Status',
            'allergies': 'Allergies'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'mother_Fname': forms.TextInput(attrs={'class': 'form-control'}),
            'mother_Lname': forms.TextInput(attrs={'class': 'form-control'}),
            'father_Fname': forms.TextInput(attrs={'class': 'form-control'}),
            'father_Lname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'fee': forms.NumberInput(attrs={'class': 'form-control'}),
            'fee_status': forms.Select(attrs={'class': 'form-control'}, choices=Student.FEE_STATUS_CHOICES),
            'student_status': forms.Select(attrs={'class': 'form-control'}, choices=Student.STUDENT_STATUS_CHOICES),
            'allergies': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CertForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = ['name']
        widgets = {
            'name': forms.CheckboxSelectMultiple,
        }




class StaffForm(forms.ModelForm):
    certificates = forms.ModelMultipleChoiceField(
        queryset=Certification.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    class Meta:
        model = Staff
        fields = [
            'staff_first_name', 'staff_last_name', 'staff_birth_date', 'staff_email', 
            'staff_phone', 'certificates'
        ]
        labels = {
            'staff_first_name': 'First Name',
            'staff_last_name': 'Last Name',
            'staff_birth_date': 'Birth Date',
            'staff_email': 'Email',
            'staff_phone': 'Phone',
            'certificates': 'Certification'
        }
        widgets = {
                'staff_first_name': forms.TextInput(attrs={'class': 'form-control'}),
                'staff_last_name': forms.TextInput(attrs={'class': 'form-control'}),
                'staff_birth_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
                'staff_email': forms.EmailInput(attrs={'class': 'form-control'}),
                'staff_phone': forms.TextInput(attrs={'class': 'form-control'}),
        }   