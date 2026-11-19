# Archer Niemi 11-19-2026

def analyze_payroll(payroll):
    total = 0
    invalid_count = 0
    for row in range(len(payroll)):
        for col in range(len(payroll[row])):
            try:
                total += int(payroll[row][col])
            except ValueError:
                invalid_count += 1
    return [total, invalid_count]


def main():
    payroll = [["120","90","banana"],["75","unknown","105"],["50","60","80"]]
    print(analyze_payroll(payroll))

if __name__ == "__main__":
    main()