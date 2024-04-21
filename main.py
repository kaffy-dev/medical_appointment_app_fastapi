from fastapi import FastAPI
from routers.doctors import doctors_router
from routers.patient import patient_router
from routers.appointment import appointment_router


app = FastAPI()

app.include_router(doctors_router, prefix='/doctors', tags=['Doctors'])
app.include_router(patient_router, prefix='/patients', tags=['Patients'])
app.include_router(appointment_router, prefix='/appointments', tags=['Appointments'])

@app.get('/')
def home():
    return {'message': 'Welcome to my Medical Appointment Application'}