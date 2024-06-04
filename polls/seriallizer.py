from rest_framework import serializers
from .models import Signup


class USerializer(serializers.ModelSerializer):
    class Meta:
        model = Signup
        fields= "__all__"