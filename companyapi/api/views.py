from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from api.models import Patient, Prescription
from api.serializers import PatientSerializer, PrescriptionSerializer



# ViewSet for managing Patient profiles
class PatientViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Patient profiles.
    Allows CRUD operations for Patient model.
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
   

    @action(detail=True, methods=['get'], url_path='medical-history')
    def medical_history(self, request, pk=None):
        """
        Retrieves medical history (prescriptions) for a specific patient.
        """
        try:
            patient = self.get_object()  # Retrieve the patient by ID (pk)
            prescriptions = Prescription.objects.filter(patient=patient)
            serializer = PrescriptionSerializer(prescriptions, many=True)
            return Response(serializer.data)
        except Patient.DoesNotExist:
            return Response({"error": "Patient not found"}, status=404)
        
    @action(detail=True, methods=['get'], url_path='prescriptions')
    def get_prescriptions(self, request, pk=None):
        """
        Retrieves a list of prescriptions for a specific patient.
        """
        try:
            patient = self.get_object()  # Retrieve the patient by ID (pk)
            prescriptions = Prescription.objects.filter(patient=patient)
            serializer = PrescriptionSerializer(prescriptions, many=True)
            return Response(serializer.data)
        except Patient.DoesNotExist:
            return Response({"error": "Patient not found"}, status=404)   
    
        
    
# ViewSet for managing Prescriptions
class PrescriptionViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Prescriptions.
    Allows CRUD operations for Prescription model.
    """
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

    def perform_create(self, serializer):
        # Ensure patient is included in the request
        patient_id = self.request.data.get('patient')
        if not patient_id:
            raise ValueError("Patient ID is required.")
        serializer.save()

    @action(detail=True, methods=['post'], url_path='renew', url_name='renew-prescription')
    def renew_prescription(self, request, pk=None):
        """
        Renews an existing prescription by duplicating it with a new status and/or updated details.
        """
        try:
            prescription = self.get_object()  # Retrieve the prescription by ID (pk)
            # Clone the prescription and adjust necessary fields (e.g., status)
            renewed_prescription = Prescription(
                patient=prescription.patient,
                medication_details=prescription.medication_details,
                dosage=prescription.dosage,
                duration=prescription.duration,  # You might adjust duration or other fields if necessary
                status='Active',  # Renewed status
            )
            renewed_prescription.save()
            serializer = PrescriptionSerializer(renewed_prescription)
            return Response(serializer.data, status=201)  # Return the newly created renewed prescription
        except Prescription.DoesNotExist:
            return Response({"error": "Prescription not found"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=400)    
        




    