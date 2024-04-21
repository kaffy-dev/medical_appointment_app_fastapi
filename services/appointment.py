from fastapi import HTTPException,status

from schema.appointment import appointments, Appointments, AppointmentCreate, AppointmentStatus
from schema.patient import patients, Patients
from utils.doctors import DoctorHelpers
from utils.appointment import AppointmentHelpers

class AppointmentService:
    
    @staticmethod
    def create_appointment(payload: AppointmentCreate):
        assigned_doctors = []
        id = len(appointments)
        
        if payload.patient not in patients:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Patient not found')
        patient: Patients = patients[payload.patient]
        
        doctor = DoctorHelpers.get_first_available_doctor()
        
        appointment = Appointments(
            id=id,
            patient=patient,
            doctor=doctor,
            date=payload.date
        )

        doctor.is_available = False
        assigned_doctors.append(doctor)
        appointments.append(appointment)
        
        return appointment
    
    @staticmethod
    def complete_appointment(appointment_id):
        appointment = AppointmentHelpers.get_appointment_by_id(appointment_id)
        if not appointment:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Appointment not made')
        
        appointment.status = AppointmentStatus.completed.value
        doctor = appointment.doctor

        if doctor:
            doctor.is_available = True
        return doctor
    
    @staticmethod
    def cancel_appointment(appointment_id):
        appointment = AppointmentHelpers.get_appointment_by_id(appointment_id)
        if not appointment:
            raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail="Appointment not made")
        appointments.remove(appointment)
        doctor = appointment.doctor
        doctor.is_available = True
        return appointment
