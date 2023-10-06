from django.shortcuts import render, redirect
from .models import Student, Staff, Certification
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from .forms import StudentForm, StaffForm, IncidentForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@login_required(login_url="/accounts/login/")
def index(request):
	return render(request, 'students/index.html', {
		'students':Student.objects.all()
	})



@login_required(login_url="/accounts/login/")
def view_student(request, id):
	student = Student.objects.get(pk=id)
	return HttpResponseRedirect(reverse('index'))




@login_required(login_url="/accounts/login/")
def add(request):
	if request.method == 'POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			new_first_name = form.cleaned_data['first_name']
			new_last_name = form.cleaned_data['last_name']
			new_birth_date = form.cleaned_data['birth_date']
			new_mother_Fname = form.cleaned_data['mother_Fname']
			new_mother_Lname = form.cleaned_data['mother_Lname']
			new_father_Fname = form.cleaned_data['father_Fname']
			new_father_Lname = form.cleaned_data['father_Lname']
			new_email = form.cleaned_data['email']
			new_phone = form.cleaned_data['phone']
			new_fee = form.cleaned_data['fee']
			new_fee_status = form.cleaned_data['fee_status']
			new_student_status = form.cleaned_data['student_status']
			new_allergies = form.cleaned_data['allergies']

			new_student = Student(
				first_name = new_first_name,
				last_name = new_last_name,
				birth_date = new_birth_date,
				mother_Fname = new_mother_Fname,
				mother_Lname = new_mother_Lname,
				father_Fname = new_father_Fname,
				father_Lname = new_father_Lname	,
				email = new_email,
				phone = new_phone,
				fee = new_fee,
				fee_status = new_fee_status,
				student_status = new_student_status,
				allergies = new_allergies,
			)
			new_student.save()
			return render(request, 'students/add.html', {
				'form': StudentForm(),
				'success': True
			})
	else:
		form = StudentForm()
	return render(request, 'students/add.html', {
		'form': StudentForm()
		})



@login_required(login_url="/accounts/login/")
def edit(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'students/edit.html', {
                'form': form,
                'success': True
            })
    else:
        student = Student.objects.get(pk=id)
        form = StudentForm(instance=student)
    return render(request, 'students/edit.html', {
        'form': form
    })




@login_required(login_url="/accounts/login/")
def delete(request, id):
	if request.method == "POST":
		student = Student.objects.get(pk=id)
		student.delete()
	return HttpResponseRedirect(reverse('index'))



def staff(request):
	return render(request, 'students/staff.html', {
		'staff':Staff.objects.all()
	})



def view_staff(request, id):
	staff = Staff.objects.get(pk=id)
	return HttpResponseRedirect(reverse('index'))



def edit_staff(request, id):
    if request.method == 'POST':
        staff_members = Student.objects.get(pk=id)
        form = StaffForm(request.POST, instance=staff_members)
        if form.is_valid():
            form.save()
            return render(request, 'students/edit_staff.html', {
                'form': form,
                'success': True
            })
    else:
        staff_members = Staff.objects.get(pk=id)
        form = StaffForm(instance=staff_members)
    return render(request, 'students/edit_staff.html', {
        'form': form
    })



def delete_staff(request, id):
	if request.method == "POST":
		staff_members = Staff.objects.get(pk=id)
		staff_members.delete()
	return HttpResponseRedirect(reverse('index'))


def add_staff(request):
	if request.method == 'POST':
		form = StaffForm(request.POST)
		if form.is_valid():
			new_staff_first_name = form.cleaned_data['staff_first_name']
			new_staff_last_name = form.cleaned_data['staff_last_name']
			new_staff_birth_date = form.cleaned_data['staff_birth_date']
			new_staff_email = form.cleaned_data['staff_email']
			new_staff_phone = form.cleaned_data['staff_phone']
			new_certificates = form.cleaned_data['certificates']
			

			new_staff = Staff(
				staff_first_name = new_staff_first_name,
				staff_last_name = new_staff_last_name,
				staff_birth_date = new_staff_birth_date,
				staff_email = new_staff_email,
				staff_phone = new_staff_phone,
				certificates = new_certificates,
				
			)
			new_staff.save()
			return render(request, 'students/add_staff.html', {
				'form': StaffForm(),
				'success': True
			})
	else:
		form = StaffForm()
	return render(request, 'students/add_staff.html', {
		'form': StaffForm()
		})




@login_required(login_url="/accounts/login/")
@csrf_exempt
def notify_incident(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        incident_report = request.POST.get('message')
        # Prepare the letter
        letter = f"""
        Dear Mr./Mrs/Ms. {student.last_name}:

        This serves as notice that your child, {student.first_name} {student.last_name},

        {incident_report}

        Please feel free to contact the school for any question(s), that you may have regarding this notice.

        Yours truly;
        """
        send_mail(
            'Incident Report',
            letter,
            'jahdaiscare@gmail.com',
            [student.email],
        )
        return redirect('index')  # Redirect to index after sending the email
    return render(request, 'students/notify_incident.html', {'student': student})