from rest_framework import serializers
from .models import Factura

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = ('id', 'nrofact', 'fechaEmis', 'nomCli', 'rucCli', 'dirRecep')
        read_only_fields = ('id',)
