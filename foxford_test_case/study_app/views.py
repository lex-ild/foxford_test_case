from rest_framework import generics

from .models import Teacher, Course, Webinar, Salary
from .serializers import TeacherSerializer, CourseSerializer, WebinarSerializer, SalarySerializer


class TeacherListCreateView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class WebinarListCreateView(generics.ListCreateAPIView):
    queryset = Webinar.objects.all()
    serializer_class = WebinarSerializer


class WebinarDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Webinar.objects.all()
    serializer_class = WebinarSerializer


class SalaryListView(generics.ListAPIView):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer


class SalaryDetailView(generics.RetrieveAPIView):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer

