from django.http import HttpResponse
from modelo import serializers
from modelo import models
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from rest_framework import mixins
from rest_framework import generics
 
class CitaMedica(generics.ListCreateAPIView):
    queryset = models.CitaMedica.objects.all()
    serializer_class = serializers.CitaMedicaSerializer

class CitaMedica_detalle(generics.RetrieveUpdateAPIView):
    queryset = models.CitaMedica.objects.all()
    serializer_class = serializers.CitaMedicaSerializer

class Paciente(generics.ListCreateAPIView):
    queryset = models.Paciente.objects.all()
    serializer_class = serializers.PacienteSerializer

class Paciente_detalle(generics.RetrieveUpdateAPIView):
    queryset =  models.Paciente.objects.all()
    serializer_class = serializers.PacienteSerializer

class Medico(generics.ListCreateAPIView):
    queryset = models.Medico.objects.all()
    serializer_class = serializers.MedicoSerializer

class Medico_detalle(generics.RetrieveUpdateAPIView):
    queryset = models.Medico.objects.all()
    serializer_class = serializers.MedicoSerializer

