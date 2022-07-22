from dataclasses import fields
import imp
from rest_framework import serializers
from .models import Contributor, Musical


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = ["name"]


class MusicalSerializer(serializers.ModelSerializer):
    contributors = ContributorSerializer(many=True)

    class Meta:
        model = Musical
        fields = ["iswc", "title", "contributors"]
