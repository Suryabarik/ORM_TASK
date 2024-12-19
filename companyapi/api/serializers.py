from rest_framework import serializers
from api.models import Patient, Prescription

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'

    def validate(self, data):
        # Ensure the patient field is not null
        if not data.get('patient'):
            raise serializers.ValidationError({'patient': 'This field is required.'})
        return data
        