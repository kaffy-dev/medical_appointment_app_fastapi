from schema.patient import patients

class PatientHelpers:

    @staticmethod
    def get_patient_by_id(patient_id: int):
        patient = patients.get(patient_id)
        if patient is not None:
                return patient
        return None