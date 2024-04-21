from fastapi import HTTPException, status

from schema.doctors import doctors, DoctorsCreate, Doctors, DoctorsUpdate, DoctorStatus
from utils.doctors import DoctorHelpers

class DoctorService:

    @staticmethod
    def get_doctor_by_id(doctor_id):
        doctor = DoctorHelpers.get_doctor_by_id(doctor_id)
        if not doctor:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Doctor not found')
        return doctor
    
    @staticmethod
    def add_doctor(payload: DoctorsCreate):
        id = len(doctors)
        doctor = Doctors(
            id=id,
            **payload.model_dump()
        )

        doctors.append(doctor)
        return doctor
    
    @staticmethod
    def edit_doctor(doctor_id: int, payload:DoctorsUpdate):
        doctor: Doctors = DoctorHelpers.get_doctor_by_id(doctor_id)
        if not doctor:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Doctor not found')
        
        if payload.name:
            doctor.name = payload.name
        if payload.specialization:
            doctor.specialization = payload.specialization
        if payload.phone:
            doctor.phone = payload.phone
        return doctor
    
    @staticmethod
    def delete_doctor(doctor_id: int):
        doctor: Doctors = DoctorHelpers.get_doctor_by_id(doctor_id)
        if not doctor:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Doctor not found')
        del doctors[doctor_id]

    @staticmethod   
    def set_doctor_availability(doctor_id: int, payload: DoctorStatus):
        doctor = DoctorHelpers.get_doctor_by_id(int(doctor_id))
        if not doctor:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Doctor not found')
        
        availability_status = payload.availability_status.lower()
        if availability_status == "available":
            doctor.is_available = True
        elif availability_status == "unavailable":
            doctor.is_available = False
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid input')
        return doctor