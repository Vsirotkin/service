from rest_framework import serializers
from .models import TODO, Project


class ProjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class TODOModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TODO
        fields = '__all__'
