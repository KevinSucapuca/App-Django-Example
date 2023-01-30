
from rest_framework import serializers

class SerieSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    descripcion = serializers.CharField()