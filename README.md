This repository contains a medical appointment application built using FastAPI. The application has the following entities:

Patient: id, name, age, sex, weight, height, phone

Doctors: id, name, specialization, phone, is_available (defaults to True)

Appointment: id, patient, doctor, date

The application is to facilitate appointment bookings between patients and doctors.
- The application contains CRUD endpoints for doctors and patients. 
- Only patients can create an appointment and when a patient tries to create an appointment, the first available doctor is assigned to the appointment.
- An appointment can be completed; doing this will make the doctor available again for booking by other patients.
- An appointmment can be cancelled, making the doctor available again.
- Doctors can also set their status to unavailable to prevent them from being booked.

  To run the server,input the command below in your terminal
  uvicorn main:app --reload

  To access the API docs provided by swagger, add "/docs" to the url of the running server.
