from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from user.forms import ContactForm
from .models import Post
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.conf import settings
import datetime
import os


'''def home(request):

	context = {
	'post': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)'''
# def PostListView(request):
# 	posts = Post.objects.all()
# 	evens_odds = sorted(posts, reverse=True, key=lambda post: post.date_posted)
# 	by_date = groupby(evens_odds, key=lambda post: post.date_posted)
# 	for date, group in by_date:
# 		print('-----')
# 		print(date)
# 		for f in group:
# 			print(f)
# 	context = {
# 	'post': by_date
# 	}
# 	return render(request, 'blog/home.html', context)

class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'post'
	ordering = ['-date_posted']
	paginate_by = 5

class UserPostListView(ListView):
	model = Post
	template_name = 'blog/user_posts.html'
	context_object_name = 'post'
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False


def resume(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())
			email=  form.cleaned_data['email_address'],
			print(email)
			print(settings.EMAIL_HOST_USER)
			rec = str(settings.EMAIL_HOST_USER)
			try:
				send_mail(subject=subject, 
						message=message,
						from_email='captainvee7@gmail.com', 
						recipient_list = (rec,) ) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')

			messages.success(request, f'Your Mail has been sent!')
			return redirect ("resume")
      
	form = ContactForm()
	return render(request, "blog/resume.html", {'form':form})

def about(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())
			email=  form.cleaned_data['email_address'][0],
			# print(email)
			# print('lfllflflfl')
			print(settings.EMAIL_HOST_USER)
			rec = str(settings.EMAIL_HOST_USER)
			try:
				send_mail(
					subject,
					message,
					email,
					['captainvee7@gmail.com'],
					fail_silently=False, 
					) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')

			messages.success(request, f'Your Mail has been sent!')
			return redirect ("resume")
      
	form = ContactForm()
	return render(request, "blog/about.html", {'form':form})

# def resume(request):
# 	if request.method == 'POST':
# 		form = UserRegistrationForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			username = form.cleaned_data.get('username')
# 			messages.success(request, f'Account created for {username}!')
# 			return redirect('resume')
# 		else:
# 			form = UserRegistrationForm()
# 	return render(request, 'blog/resume.html', {'form' : form})

# Create your views here.
