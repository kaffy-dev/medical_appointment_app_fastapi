from fastapi import APIRouter, status

from schema.patient import patients, PatientCreate, PatientUpdate
from services.patient import PatientService

patient_router = APIRouter()

@patient_router.get('/', status_code=status.HTTP_200_OK)
def list_all_patients():
    data = PatientService.parse_patients(patient_data=patients)
    return {'message': 'success', 'data': data}

@patient_router.get('/{patient_id}', status_code=status.HTTP_200_OK)
def get_patient_by_id(patient_id: int):
    data = PatientService.get_patient_by_id(patient_id)
    return {'message': 'success', 'data': data}

@patient_router.post('/', status_code=status.HTTP_201_CREATED)
def add_patient(payload: PatientCreate):
    data = PatientService.add_patient(payload)
    return {'message': 'Patient added successfully', 'data': data}

@patient_router.put('/{patient_id}', status_code=status.HTTP_200_OK)
def edit_patient(patient_id: int, payload: PatientUpdate):
    data = PatientService.edit_patient(patient_id, payload)
    return {'message': 'Patient updated successfully', 'data': data}

@patient_router.delete('/{patient_id}', status_code=status.HTTP_404_NOT_FOUND)
def delete_patient(patient_id: int):
    PatientService.delete_patient(patient_id)
    return {'message': 'Patient deleted successfully'}