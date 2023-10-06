from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('<int:id>', views.view_student, name='view_student'),
	path('add/', views.add, name='add'),
	path('edit/<int:id>/', views.edit, name='edit'),
	path('delete/<int:id>/', views.delete, name='delete'),
	# Staff urls
	path('staff/', views.staff, name='staff'),
	path('<int:id>/',  views.view_staff, name='view-staff'),
	path('add_staff/', views.add_staff, name='add-staff'),
	path('edit_staff/<int:id>/', views.edit_staff, name='edit-staff'),
	path('delete_staff/<int:id>/', views.delete_staff, name='delete-staff'),
	path('notify_incident/<int:student_id>/', views.notify_incident, name='notify_incident'),

]