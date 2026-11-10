# Archer Niemi 11-10-2026

def findInvalidTransactions(transactions, accounts):
    invalidTransactions = []
    for i,transaction in enumerate(transactions):
        if not validTransation(transaction,accounts):
            invalidTransactions.append(i)
    return invalidTransactions

def validTransation(transaction, accounts):
    try:
        accounts[transaction[0]]
        accounts[transaction[1]]
        if int(transaction[2]) < 0:
            raise ValueError
    except KeyError:
        return False
    except ValueError:
        return False

    return True

def findSuspiciousTransations(transactions, accounts):
    invalidTransactions = findInvalidTransactions(transactions, accounts)

    suspiciousTransations = []

    for i,transaction1 in enumerate(transactions):
        if i in invalidTransactions:
            continue

        for j,transaction2 in enumerate(transactions[i:]):
            if reciprocal(transaction1) == transaction2:
                suspiciousTransations.append((i,j))
    
    return suspiciousTransations

def reciprocal(transaction):
    return [transaction[1],transaction[0],transaction[2]]

def main():
    transactions = [
        ["F", "P", "40"],
        ["P", "F", "40"],
        ["F", "G", "oops"],
        ["G", "F", "20"],
        ["X", "P", "40"],
        ["P", "F", "40"]
    ]

    accounts = {"F": "Floppsie", "P": "Peter", "G": "Goldhoarder"}

    print(findSuspiciousTransations(transactions, accounts))

if __name__ == "__main__":
    main()