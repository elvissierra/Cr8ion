from rest_framework import serializers
from .models import Print

class  PrintSerializer(serializers.ModelSerializer):

    class Meta:
        model = Print
        fields = "__all__"

        