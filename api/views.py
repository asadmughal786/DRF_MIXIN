# =================================================GenericAPIView and ModelMixin============================================================
from django.shortcuts import render
from .models import studentModel
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin


# Create your views here.
# =========================================== Generic with Mixin ===============================

# class LCStudent(GenericAPIView, ListModelMixin, CreateModelMixin):
#     queryset = studentModel.objects.all()
#     serializer_class = StudentSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class RUDStudent(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     queryset = studentModel.objects.all()
#     serializer_class = StudentSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# ========================================= Concrete API View Using Generics(ListAPIView,Update) ===========================
# There are more Views as well ()
class StudentList(ListAPIView):
    queryset = studentModel.objects.all()
    serializer_class = StudentSerializer


class StudentCreate(CreateAPIView):
    queryset = studentModel.objects.all()
    serializer_class = StudentSerializer


class StudentRetrieve(RetrieveAPIView):
    queryset = studentModel.objects.all()
    serializer_class = StudentSerializer


class StudentUpdate(UpdateAPIView):
    queryset = studentModel.objects.all()
    serializer_class = StudentSerializer

class StudentDestroy(DestroyAPIView):
    queryset = studentModel.objects.all()
    serializer_class= StudentSerializer