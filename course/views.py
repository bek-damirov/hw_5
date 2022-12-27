from rest_framework import generics
from rest_framework import viewsets
from .models import *
from .serializers import StudentSerializer, MentorSerializer, CourseSerializer
from .generic import ListMixinAPI, CreateMixinAPI, RetrieveMixinApi, UpdateMixinAPI, DeleteMixinAPI, MyApiView


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class StudentCreateListView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class MentorUniversalViewSet(ListMixinAPI, CreateMixinAPI, RetrieveMixinApi, UpdateMixinAPI, DeleteMixinAPI,
                             viewsets.ViewSetMixin, MyApiView):
    serializer_class = MentorSerializer
    model = Mentor
    queryset = Mentor.objects.all()
