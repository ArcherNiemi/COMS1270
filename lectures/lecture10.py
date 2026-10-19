# Archer Niemi 10-15-2026

def main():
    results = {"FOX": 7,"WOLF": 9, "BUNNY": 9, "BEAR": 6}
    print(determineWinners(results))

def determineWinners(results):
    winners = {}
    maxVotes = max(results.values())
    for (name,votes) in results.items():
        if votes >= maxVotes:
            winners.update({name: votes})
    return winners

if __name__ == "__main__":
    main()