from rest_framework import generics

from .models import Character
from .permissions import IsAuthorOrReadOnly
from .serializers import CharacterSerializer

class CharacterList(generics.ListCreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class CharacterDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
