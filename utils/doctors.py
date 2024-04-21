from fastapi import HTTPException, status

from schema.doctors import doctors
from schema.appointment import appointments


class DoctorHelpers:

    @staticmethod
    def get_doctor_by_id(doctor_id: int):
        for doctor in doctors:
            if doctor.id == doctor_id:
                return doctor
        return None
    
    @staticmethod
    def assigned_doctors():
        assigned_docs = []
        for appointment in appointments:
            if appointment.doctor in assigned_docs:
               assigned_docs.append(appointment.doctor)
        return assigned_docs
           
    @staticmethod
    def get_first_available_doctor():
        assigned_docs = DoctorHelpers.assigned_doctors()
        for doctor in doctors:
            if len(doctors) == 0:
                raise HTTPException(
                    status_code=status.HTTP_503_SERVICE_UNAVAILABLE, 
                    detail='No available doctor'
                )
            
            elif len(doctors) == 1:
                if doctor in assigned_docs or doctor.is_available == False:
                    raise HTTPException(
                    status_code=status.HTTP_503_SERVICE_UNAVAILABLE, 
                    detail='No available doctor'
                )
                return doctor

            else:
                if doctor.is_available and doctor not in assigned_docs:
                    return doctor
        raise HTTPException(
                    status_code=status.HTTP_503_SERVICE_UNAVAILABLE, 
                    detail='No available doctor'
        )
        