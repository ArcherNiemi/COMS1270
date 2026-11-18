"""Peter's Catastrophic Payroll System — student starter file.

Complete the five TODO functions. Do not change their names or parameters.
"""


def parse_employee(record):
    """Return a new dictionary with name, float hours, and float rate.

    Convert numeric values using float(). If a conversion raises ValueError
    or TypeError, raise ValueError('Invalid numeric payroll data.').
    Allow missing keys (KeyError) to propagate.
    """
    newRecord = {}
    try:
        newRecord["name"] = record["name"]
        newRecord["hours"] = float(record["hours"])
        newRecord["rate"] = float(record["rate"])
    except (ValueError, TypeError):
        raise ValueError('Invalid numeric payroll data.')
    return newRecord

def validate_employee(employee):
    """Return True for a valid employee, otherwise raise ValueError.

    Check name, hours, and rate, in that order. Exact error messages:
    'Invalid employee name.'
    'Invalid working hours.'
    'Invalid hourly rate.'
    """

    try:
        if type(employee["name"]) != str or employee["name"] == "":
            raise ValueError
    except:
        raise ValueError("Invalid employee name.")

    try:
        if employee["hours"] < 0 or employee["hours"] > 80:
            raise ValueError
    except:
        raise ValueError("Invalid working hours.")

    try:
        if employee["rate"] <= 0 or employee["rate"] > 500:
            raise ValueError
    except:
        raise ValueError("Invalid hourly rate.")

    return True


def calculate_pay(employee):
    if employee["hours"] > 40:
        return 40 * employee["rate"] + (employee["hours"] - 40) * employee["rate"] * 1.5
    else:
        return employee["hours"] * employee["rate"]

def process_employee(record, summary):
    """Return a PAID or REJECTED result; update summary counters.

    Use try/except/else/finally. Catch ValueError, TypeError, KeyError.
    Count every attempt in finally, including rejected records.
    """
    rejected = False
    try:
        employee = parse_employee(record)
        valid_employee = validate_employee(employee)
        pay = calculate_pay(employee)
    except (ValueError, TypeError, KeyError) as e:
        summary["rejected"] += 1
        rejected = True
        error = e
    else:
        summary["successful"] += 1
        rejected = False
    finally:
        summary["attempted"] += 1

    if not rejected:
        return {"name": employee["name"],"status": "PAID","pay": pay}
    else:
        try:
            return {"name": record["name"],"status": "REJECTED","error": str(error)}
        except:
            return {"name": "Unknown","status": "REJECTED","error": str(error)}

def process_payroll(records):
    summary = {"attempted": 0,"successful": 0,"rejected":0}
    results = []
    totalPay = 0
    for record in records:
        result = process_employee(record, summary)
        results.append(result)
        if result["status"] == "PAID":
            totalPay += result["pay"]
    return {"summary": summary, "results": results, "total_pay": totalPay}
    pass
