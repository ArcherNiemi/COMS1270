"""Student-facing pytest tests; hidden Gradescope tests may cover more cases."""
from investigation import Employee, AccessRecord, Investigation
from main import make_investigation


def small_case():
    employees = [
        Employee(1, "Alice", "A", 2, ["Office", "Records Room"]),
        Employee(2, "Bob", "B", 3, ["Office", "Server Room"]),
        Employee(3, "Carol", "C", 1, ["Office"]),
    ]
    rooms = {"Office": 1, "Records Room": 2, "Server Room": 3, "Vault": 5}
    records = [
        AccessRecord(1, "Records Room", 600, True),
        AccessRecord(1, "Server Room", 1320, False),
        AccessRecord(1, "Vault", 1350, False),
        AccessRecord(2, "Server Room", 1330, True),
        AccessRecord(2, "Vault", 1360, False),
        AccessRecord(3, "Office", 600, True),
        AccessRecord(3, "Server Room", 1340, True),
        AccessRecord(3, "Vault", 1400, False),
    ]
    return Investigation(employees, records, rooms)


def test_employee_constructor_and_authorization():
    employee = Employee(5, "Test", "Support", 2, ["Office"])
    assert employee.employee_id == 5
    assert employee.name == "Test"
    assert employee.department == "Support"
    assert employee.clearance == 2
    assert employee.authorized_rooms == ["Office"]
    assert employee.can_enter("Office") is True
    assert employee.can_enter("Vault") is False


def test_suspicious_rules():
    case = small_case()
    assert case.is_suspicious(case.records[0]) is False
    assert case.is_suspicious(case.records[1]) is True
    assert case.is_suspicious(case.records[3]) is True
    assert case.is_suspicious(case.records[5]) is False
    # Clearance bypass during business hours, even when authorization is granted.
    extra = AccessRecord(3, "Vault", 600, True)
    assert case.is_suspicious(extra) is True
    # Exactly 6 PM is not after hours.
    assert case.is_suspicious(AccessRecord(2, "Server Room", 1080, True)) is False


def test_suspects():
    case = small_case()
    assert [person.name for person in case.find_suspects()] == ["Alice", "Bob", "Carol"]


def test_shared_visit_helper():
    case = small_case()
    assert case.shared_suspicious_visit(case.employees[0], case.employees[2]) is True
    assert case.shared_suspicious_visit(case.employees[0], case.employees[1]) is True


def test_spy_teams():
    case = small_case()
    teams = case.find_spy_teams()
    assert [(a.name, b.name) for a, b in teams] == [("Alice", "Bob"), ("Alice", "Carol"), ("Bob", "Carol")]


def test_full_mystery():
    case = make_investigation()
    assert len(case.employees) == 10
    assert len(case.records) == 26
    assert [e.name for e in case.find_suspects()] == ["Felicity", "Harold", "Mildred", "Doris", "Bernard", "Iris"]
    assert [(a.name, b.name) for a, b in case.find_spy_teams()] == [
        ("Felicity", "Doris"), ("Harold", "Iris")
    ]
