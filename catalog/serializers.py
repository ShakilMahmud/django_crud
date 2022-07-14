from dataclasses import fields
from rest_framework import serializers
from .models import Task


class TashSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
