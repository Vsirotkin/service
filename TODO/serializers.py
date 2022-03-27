from rest_framework import serializers
from .models import Project, TODO


class ProjectModelSerializer(serializers.ModelSerializer):
    usernames = serializers.StringRelatedField(many=True)
    class Meta:
        model = Project
        fields = '__all__'


class TODOModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TODO
        fields = '__all__'
