from fastapi import APIRouter, status

from schema.appointment import appointments, AppointmentCreate
from services.appointment import AppointmentService

appointment_router = APIRouter()

@appointment_router.get('/', status_code=status.HTTP_200_OK)
def list_all_appointments():
    return {'message': 'success', 'data': appointments}

@appointment_router.post('/', status_code=status.HTTP_201_CREATED)
def create_appointment(payload: AppointmentCreate):
    data = AppointmentService.create_appointment(payload)
    return {'message': 'Appointment created successfully', 'data': data}

@appointment_router.put('/', status_code=status.HTTP_200_OK)
def complete_appointment(appointment_id: int):
    data = AppointmentService.complete_appointment(appointment_id)
    return {'message': 'Appointment completed successfully', 'data': data}

@appointment_router.delete('/{appointment_id}', status_code=status.HTTP_200_OK)
def cancel_appointment(appointment_id: int):
    AppointmentService.cancel_appointment(appointment_id)
    return {'message': 'Appointment cancelled successfully'}
