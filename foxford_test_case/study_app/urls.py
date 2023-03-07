from django.urls import path
from django.views.generic import TemplateView

from .views import TeacherListCreateView, TeacherDetailView, CourseListCreateView, CourseDetailView,\
    WebinarListCreateView, WebinarDetailView, SalaryListView, SalaryDetailView
from .models import Teacher
from .serializers import TeacherSerializer


urlpatterns = [
    path('teachers/', TeacherListCreateView.as_view(), name='teacher-list-create'),
    path('teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher-detail'),
    path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('webinars/', WebinarListCreateView.as_view(), name='webinar-list-create'),
    path('webinars/<int:pk>/', WebinarDetailView.as_view(), name='webinar-detail'),
    path('salaries/', SalaryListView.as_view(), name='salary-list'),
    path('salaries/<int:pk>/', SalaryDetailView.as_view(), name='salary-detail'),
    path('swagger-ui/', TemplateView.as_view(
            template_name='swagger-ui.html',
            extra_context={'schema_url': 'openapi-schema'}
        ), name='swagger-ui'),
]
