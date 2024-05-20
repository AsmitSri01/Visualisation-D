from rest_framework import serializers
from .models import Dashboard_data

class Dashboard_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Dashboard_data
        fields='__all__'