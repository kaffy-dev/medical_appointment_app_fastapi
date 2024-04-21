from schema.appointment import appointments

class AppointmentHelpers:

    @ staticmethod
    def get_appointment_by_id(appointment_id):
        for appoint in appointments:
            if appoint.id == appointment_id:
                return appoint
        return None