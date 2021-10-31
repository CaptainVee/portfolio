from django.urls import path
from . import views
from .views import AttendProfileCreateView, AttendanceListView

urlpatterns = [
path('attendance/', AttendanceListView.as_view(), name='attendance-list'),
path('attendance/new/', AttendProfileCreateView.as_view(), name='attendance-create'),
# path('', views.about, name='blog-about'),

]