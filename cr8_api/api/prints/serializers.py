from rest_framework import serializers
from apps.prints.models import Print

class  PrintSerializer(serializers.ModelSerializer):

    class Meta:
        model = Print
        fields = "__all__"

        