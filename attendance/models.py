from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.


CHOICES = (
	('Worker', 'Worker'),
	('Non-worker', 'Non-Worker'),
		)

LEVEL = (
	('100', '100'),
	('200', '200'),
	('300', '300'),
	('400', '400'),
	('500', '500'),
	('other', 'Other'),
		)

GENDER = (
	('Male', 'Male'),
	('Female', 'Female'),
		)

TITLE = (
	('Bro', 'Bro'),
	('Sis', 'Sis'),
		)

class AttendProfile(models.Model):
	title = models.CharField(max_length=5, choices=TITLE)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	middle_name = models.CharField(max_length=50, blank=True, null=True)
	picture = models.ImageField(default='default.jpg', upload_to='profile_pics', blank=True, null=True)
	# profile_pic = models.ImageField(upload_to='watchman_pics', default='watchman_pics/index.jpg', blank=True, null=True)
	gender = models.CharField(max_length=10, choices=GENDER)
	whatsapp_number = models.CharField(max_length=12)
	phone_number = models.CharField(max_length=12, blank=True, null=True)
	residence = models.CharField(max_length=150, blank=True, null=True)
	bio = models.CharField(max_length=500, blank=True, null=True)
	is_worker = models.CharField(max_length=20, choices=CHOICES)
	position = models.CharField(max_length=100, blank=True, null=True)
	birthday = models.DateField(blank=True, null=True)
	department = models.CharField(max_length=100, blank=True, null=True)
	level = models.CharField(max_length=20, choices=LEVEL)
	home_address = models.CharField(max_length=100, blank=True, null=True)
	home_church = models.CharField(max_length=100, blank=True, null=True)
	next_of_kin_name = models.CharField(max_length=50, blank=True, null=True)
	next_of_kin_number = models.CharField(max_length=12, blank=True, null=True)
	created_at = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title + self.first_name + self.last_name

	def get_absolute_url(self):
		return reverse('attendance-list')



