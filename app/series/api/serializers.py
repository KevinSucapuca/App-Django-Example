
from rest_framework import serializers
from series.models import Serie
class SerieSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Serie
        fields = '__all__'
