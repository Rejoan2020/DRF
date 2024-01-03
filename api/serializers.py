from rest_framework import serializers
from rapi.models import Student

class studentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'