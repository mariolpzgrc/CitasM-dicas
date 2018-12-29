from rest_framework import serializers
from modelo import models


class CitaMedicaSerializer(serializers.ModelSerializer):
    def validate_hora(self, hora):
        if hora != 30:
            raise serializers.ValidationError(
                "La hora no puede pasar de los 30 minutos")
        return hora

    def validate(self, data):
        listahora = models.Cita.objects.filter(hora=data['hora'])
        listadia = models.Cita.objects.filter(dia=data['dia'])
        if len(listahora) != 0 and len(listadia) != 0:
            raise serializers.ValidationError("La hora ya esta asignada")
        return data

    class Meta:
        model = models.CitaMedica
        fields = ('id', 'dia', 'hora', 'paciente', 'medico')


class PacienteSerializer(serializers.ModelSerializer):
    def validate_paciente(self, data):
        lista = models.Paciente.objects.filter(nombre=data['nombre'])
        listaap = models.Paciente.objects.filter(
            apellidoPaterno=data['apellidoPaterno'])
        listaam = models.Paciente.objects.filter(
            apellidoMaterno=data['apellidoMaterno'])

        if len(lista) != 0 and len(listaap) != 0 and len(listaam) != 0:
            raise serializers.ValidationError(
                "El nombre del paciente no debe estar reppetido")
        return data

        class Meta:
            model = models.Paciente
            fields = ('id', 'nombre', 'apellidoPaterno',
                      'apellidoMaterno', 'fechaNacimiento', 'talla', 'peso')


class MedicoSerializer(serializers.ModelSerializer):
    def validate_medico(self, data):
        listanombre = models.Medico.objects.filter(nombre=data['nombre'])
        listaapp = models.Medico.objects.filter(
            apellidoPaterno=data['apellidoPaterno'])
        listaapm = models.Medico.objects.filter(
            apellidoMaterno=data['apellidoMaterno'])

        if len(listanombre) != 0 and len(listaapp) != 0 and len(listaapm) != 0:
            raise serializers.ValidationError(
                "EL nombre del médico no debe estar repetido")
        return data

        class Meta:
            model = models.Medico
            fields = ('id', 'nombre', 'apellidoPaterno',
                      'apellidoMaterno', 'usuario', 'contraseña')
