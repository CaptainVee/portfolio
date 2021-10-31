from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import AttendProfile
# Create your views here.


class AttendProfileCreateView(CreateView):
	model = AttendProfile
	fields = [	'title',
				'first_name',
				'last_name',
				'middle_name',
				'profile_pic',
				'gender',
				'whatsapp_number',
				'phone_number',
				'residence',
				'bio',
				'is_worker',
				'position',
				'birthday',
				'department',
				'level',
				'home_address',
				'home_church',
				'next_of_kin_name',
				'next_of_kin_number',
				]

	def form_valid(self, form):
		return super().form_valid(form)


class AttendanceListView(ListView):
	model = AttendProfile
	template_name = 'attendance/attendance_list.html'
	context_object_name = 'post'
	ordering = ['-created_at']
	paginate_by = 20
