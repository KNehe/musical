from rest_framework import generics

from musicals.models import Musical
from musicals.serializers import MusicalSerializer


class MusicalRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Musical.objects.all().prefetch_related()
    serializer_class = MusicalSerializer
    lookup_field = "iswc"
