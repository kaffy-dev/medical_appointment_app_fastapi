from fastapi import HTTPException, status

from schema.patient import patients, Patients, PatientCreate, PatientUpdate
from utils.patient import PatientHelpers

class PatientService:

    @staticmethod
    def parse_patients(patient_data):
        data = []
        for pat in patient_data:
            data.append(patients[pat])
        return data
    
    @staticmethod
    def get_patient_by_id(patient_id):
        patient = PatientHelpers.get_patient_by_id(patient_id)
        if not patient:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Patient not found'
            )
        return patient
    
    @staticmethod
    def add_patient(payload: PatientCreate):
        id = len(patients)
        patient = Patients(
            id=id,
            **payload.model_dump()
        )
        patients[id] = patient
        return patient
    
    @staticmethod
    def edit_patient(patient_id: int, payload: PatientUpdate):
        patient = PatientHelpers.get_patient_by_id(patient_id)
        if not patient:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Patient not found")
        if payload.name:
            patient.name = payload.name
        if payload.age:
            patient.age = payload.age
        if payload.sex:
             patient.sex = payload.sex
        if payload.weight:
             patient.weight = payload.weight
        if payload.height:
             patient.height = payload.height
        if payload.phone:
             patient.phone = payload.phone
        
        return patient
    
    @staticmethod
    def delete_patient(patient_id):
        patient = PatientHelpers.get_patient_by_id(patient_id)
        if not patient:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Patient not found')
        del patients[patient_id]