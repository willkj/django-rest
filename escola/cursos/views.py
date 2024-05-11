from rest_framework.response import Response
from rest_framework import generics
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer

class CursosAPIView(generics.ListCreateAPIView):
    queryset= Curso.objects.all()
    serializer_class = CursoSerializer

#class CursoAPIView():


# class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):

    
class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset= Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

# class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):


