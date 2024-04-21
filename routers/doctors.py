from fastapi import APIRouter, status, Path

from schema.doctors import doctors, DoctorsCreate, DoctorsUpdate, DoctorStatus
from services.doctors import DoctorService

doctors_router = APIRouter()

@doctors_router.get('/', status_code=status.HTTP_200_OK)
def list_all_doctors():
    return {'message': 'success', 'data': doctors}

@doctors_router.get('/{doctor_id}', status_code=status.HTTP_200_OK)
def get_doctor_by_id(doctor_id: int):
    data = DoctorService.get_doctor_by_id(doctor_id)
    return {'message': 'success', 'data': data}

@doctors_router.post('/', status_code=status.HTTP_201_CREATED)
def add_doctor(payload: DoctorsCreate):
    data = DoctorService.add_doctor(payload)
    return {'message': 'Doctor added successfully', 'data': data}

@doctors_router.put('/{doctor_id}', status_code=status.HTTP_200_OK)
def edit_doctor(doctor_id: int, payload:DoctorsUpdate):
    data = DoctorService.edit_doctor(doctor_id, payload)
    return {'message': 'Doctor updated successfully', 'data': data}

@doctors_router.delete('/{doctor_id}', status_code=status.HTTP_200_OK)
def delete_doctor(doctor_id: int):
    DoctorService.delete_doctor(doctor_id)
    return {'message': 'Doctor deleted successfully'}

@doctors_router.post('/status{doctor_id}', status_code=status.HTTP_201_CREATED)
def set_availability_status(
    *, doctor_id: int = Path(description="Input for availability status should either be available or unavailable"), 
    payload: DoctorStatus 
    ):
    data = DoctorService.set_doctor_availability(doctor_id, payload)
    return {'message': 'success', 'data': data}