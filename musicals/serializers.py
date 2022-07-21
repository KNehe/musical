from dataclasses import fields
import imp
from rest_framework import serializers
from .models import Musical


class MusicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musical
        fields = ["iswc", "title", "contributors"]
