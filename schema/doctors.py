from typing import Optional
from pydantic import BaseModel

# Doctors: id, name, specialization, phone, is_available (defaults to True)

class Doctors(BaseModel):
    id: int
    name: str
    specialization: str
    phone: str
    is_available: bool = True

class DoctorsCreate(BaseModel):
    name: str
    specialization: str
    phone: str

class DoctorsUpdate(BaseModel):
    name: Optional[str] = None
    specialization: Optional[str] = None
    phone: Optional[str] = None

class DoctorStatus(BaseModel):
    availability_status: str

doctors: list[Doctors] = [
    Doctors(
        id=0, name='Doctor 1', specialization='physiotheraphy', phone='0809', is_available=False 
    )
]