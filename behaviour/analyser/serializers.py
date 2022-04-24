from rest_framework import serializers
from .models import *

class RawDataSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
                'id',
                'media',
                )
        model = RawData

class InteractionsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('image',)
        model = Interactions

class TransitionsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('image',)
        model = Transitions

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
                'preview',
                'headers',
                'ids',
                'behaviors',
                'categories',
                )
        model = Info

class DataPlotSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('image',)
        model =  DataPlot





