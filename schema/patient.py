from typing import Optional
from pydantic import BaseModel
from decimal import Decimal

# Patient: id, name, age, sex, weight, height, phone

class Patients(BaseModel):
    id: int
    name: str
    age: int
    sex: str
    weight: Decimal
    height: Decimal
    phone: str

class PatientCreate(BaseModel):
    name: str
    age: int
    sex: str
    weight: Decimal
    height: Decimal
    phone: str

class PatientUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    sex: Optional[str] = None
    weight: Optional[Decimal] = None
    height: Optional[Decimal] = None
    phone: Optional[str] = None

patients: dict[int, Patients] = {
    0: Patients(
        id=0, name='Patient 1', age=15, sex='female', weight=Decimal(20), height=Decimal('80'), phone='0899'
    ),
    1: Patients(
        id=1, name='Patient 2', age=60, sex='male', weight=Decimal(90), height=Decimal('167'), phone='0860'
    ),
    2: Patients(
        id=2, name='Patient 3', age=25, sex='female', weight=Decimal(80), height=Decimal('189'), phone='0420'
    )
}