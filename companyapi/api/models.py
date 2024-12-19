

from django.db import models




# Patient Profile Management Models
class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)  # Unique identifier
    name = models.CharField(max_length=100)  # Personal details
    dob = models.DateField()  # Date of Birth
    contact_info = models.CharField(max_length=15)  # Contact info
    medical_history = models.TextField(blank=True, null=True)  # Medical history
    known_allergies = models.TextField(blank=True, null=True)  # Known allergies
    current_medications = models.TextField(blank=True, null=True)  # Current medications
    
    created_at = models.DateTimeField(auto_now_add=True)  # Record creation timestamp
    updated_at = models.DateTimeField(auto_now=True)  # Last updated timestamp

    def __str__(self):
        return self.name

# Digital Prescription Management Models
class Prescription(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Completed', 'Completed'),
        ('Expired', 'Expired'),
    ]

    prescription_id = models.AutoField(primary_key=True)  # Unique identifier
    #patient = models.ForeignKey(Patient, related_name='prescriptions', on_delete=models.CASCADE)  # Relationship to Patient
    patient = models.ForeignKey(
        Patient, 
        related_name='prescriptions', 
        on_delete=models.CASCADE, 
        null=False, 
        blank=False
    )
    medication_details = models.TextField()  # Details about the medications
    dosage = models.CharField(max_length=100)  # Dosage instructions
    duration = models.CharField(max_length=100)  # Duration for the prescription
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')  # Status of the prescription

    created_at = models.DateTimeField(auto_now_add=True)  # Record creation timestamp
    updated_at = models.DateTimeField(auto_now=True)  # Last updated timestamp

    def __str__(self):
        return f"Prescription {self.prescription_id} for {self.patient.name}"

# Example validations (add to forms or views as needed):
# - Ensure `dob` is in the past.
# - Prevent duplicate prescriptions for the same patient within overlapping durations.



