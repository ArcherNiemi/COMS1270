"""Provided demonstration. Run with: python main.py"""
from investigation import Employee, AccessRecord, Investigation


def make_investigation():
    rooms = {"Office": 1, "Records Room": 2, "Server Room": 3, "Vault": 5}
    employees = [
        Employee(101, "Floppsie", "Programming", 3, ["Office", "Server Room"]),
        Employee(102, "Felicity", "Marketing", 1, ["Office"]),
        Employee(103, "Peter", "Accounting", 2, ["Office", "Records Room"]),
        Employee(104, "Goldhoarder", "Management", 5, ["Office", "Records Room", "Server Room", "Vault"]),
        Employee(105, "Harold", "Programming", 2, ["Office", "Records Room"]),
        Employee(106, "Mildred", "Accounting", 3, ["Office", "Records Room", "Server Room"]),
        Employee(107, "Doris", "Marketing", 1, ["Office"]),
        Employee(108, "Bernard", "Support", 2, ["Office", "Records Room"]),
        Employee(109, "Iris", "Programming", 3, ["Office", "Server Room"]),
        Employee(110, "Quentin", "Support", 1, ["Office"]),
    ]
    # Each record is (employee ID, room, minutes after midnight, granted).
    raw = [
        (101, "Server Room", 540, True), (101, "Office", 600, True),
        (102, "Vault", 1100, False), (102, "Server Room", 1120, False), (102, "Office", 700, True),
        (103, "Records Room", 600, True), (103, "Office", 900, True),
        (104, "Vault", 720, True), (104, "Office", 1150, True),
        (105, "Server Room", 1380, True), (105, "Vault", 1410, False), (105, "Office", 800, True),
        (106, "Records Room", 1200, True), (106, "Server Room", 1230, True), (106, "Office", 750, True),
        (107, "Server Room", 1110, False), (107, "Vault", 1130, False), (107, "Office", 630, True),
        (108, "Records Room", 1270, True), (108, "Vault", 1300, False), (108, "Office", 540, True),
        (109, "Server Room", 1385, True), (109, "Vault", 1415, False), (109, "Office", 570, True),
        (110, "Office", 610, True), (110, "Records Room", 700, False),
    ]
    records = []
    for employee_id, room, time, granted in raw:
        records.append(AccessRecord(employee_id, room, time, granted))
    return Investigation(employees, records, rooms)


def main():
    investigation = make_investigation()
    print("GOLDHOARDER SOFTWARE SOLUTIONS")
    print("The Great Employee Investigation")
    print("-" * 42)
    print("Employees examined:", len(investigation.employees))
    suspicious_count = 0
    for record in investigation.records:
        if investigation.is_suspicious(record):
            suspicious_count += 1
    print("Suspicious records:", suspicious_count)
    suspects = investigation.find_suspects()
    print("Suspects:", len(suspects))
    for employee in suspects:
        print(" -", employee.name)
    teams = investigation.find_spy_teams()
    print("Possible spy teams:", len(teams))
    for first, second in teams:
        print(" -", first.name, "and", second.name)
    print("Remember: a match is not proof of guilt.")


if __name__ == "__main__":
    main()
