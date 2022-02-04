from rest_framework import serializers

from .models import Part, Line, LineData, Spare, Sub_Assembly


class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = '__all__'

class LineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Line
        fields = '__all__'

class LineDataSerializer(serializers.ModelSerializer):
    part = serializers.StringRelatedField()
    line = serializers.StringRelatedField()
    sub_assembly = serializers.StringRelatedField()
    spare = serializers.StringRelatedField()
    class Meta:
        model = LineData
        fields = '__all__'

class SpareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spare
        fields = '__all__'

class Sub_AssemblySerializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_Assembly
        fields = '__all__'