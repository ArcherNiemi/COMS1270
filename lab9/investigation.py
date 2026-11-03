"""Student work: complete the five TODO methods below."""

AFTER_HOURS = 1080
MIN_SUSPICIOUS_RECORDS = 2
MAX_TIME_DIFFERENCE = 30


class Employee:
    def __init__(self, employee_id, name, department, clearance, authorized_rooms):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.clearance = clearance
        self.authorized_rooms = authorized_rooms

    def can_enter(self, room):
        if room in self.authorized_rooms:
            return True
        return False

class AccessRecord:
    def __init__(self, employee_id, room, time, granted):
        self.employee_id = employee_id
        self.room = room
        self.time = time
        self.granted = granted


class Investigation:
    def __init__(self, employees, records, room_clearances):
        self.employees = employees
        self.records = records
        self.room_clearances = room_clearances

    def is_suspicious(self, record):
        id = record.employee_id
        employee = self.find_employee(id)
        
        if not employee.can_enter(record.room):
            return True

        if record.time > AFTER_HOURS:
            return True

        if record.granted and self.room_clearances[record.room] > employee.clearance:
            return True

        return False

    def find_employee(self, id):
        for employee in self.employees:
            if employee.employee_id == id:
                return employee
        return None

    def check_records(self, employee):
        suspect_records = 0
        for record in self.records:
            if record.employee_id == employee.employee_id and self.is_suspicious(record):
                suspect_records += 1
        return suspect_records


    def find_suspects(self):
        suspects = []
        for employee in self.employees:
            if self.check_records(employee) >= MIN_SUSPICIOUS_RECORDS:
                suspects.append(employee)
        return suspects


    def shared_suspicious_visit(self, first, second):
        """Provided helper: whether two employees have suspicious visits to the
        same room no more than MAX_TIME_DIFFERENCE minutes apart.
        """
        for first_record in self.records:
            if first_record.employee_id == first.employee_id:
                if self.is_suspicious(first_record):
                    for second_record in self.records:
                        if second_record.employee_id == second.employee_id:
                            if self.is_suspicious(second_record):
                                same_room = first_record.room == second_record.room
                                close_time = abs(first_record.time - second_record.time) <= MAX_TIME_DIFFERENCE
                                if same_room and close_time:
                                    return True
        return False

    def find_spy_teams(self):
        spy_teams = []
        suspects = self.find_suspects()
        for suspect1 in suspects:
            for suspects2 in suspects:
                if suspect1 != suspects2 and not (suspects2,suspect1) in spy_teams and self.shared_suspicious_visit(suspect1, suspects2):
                    spy_teams.append((suspect1,suspects2))
        return spy_teams