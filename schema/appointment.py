from datetime import date
from enum import Enum

from pydantic import BaseModel

from schema.patient import Patients, patients
from schema.doctors import Doctors,doctors

# Appointment: id, patient, doctor, date

class AppointmentStatus(Enum):
    completed: str = "COMPLETED"
    pending: str = "PENDING"

class Appointments(BaseModel):
    id: int
    patient: Patients
    doctor: Doctors
    date: date
    status: str = AppointmentStatus.pending.value
    
class AppointmentCreate(BaseModel):
    patient: int
    date: date

appointments: list[Appointments] = [
    Appointments(
        id=0, patient=patients[0], doctor=doctors[0], date=date(2024, 2, 17)
    )
]