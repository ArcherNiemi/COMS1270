def largest_pie_guest(num_guests):
    pie_remaining = 100
    most_taken = -1
    most_taken_person = -1
    for i in range(num_guests):
        percent_taken = (i + 1) / num_guests
        amount_taken = pie_remaining * percent_taken
        pie_remaining -= amount_taken
        if amount_taken > most_taken:
            most_taken = amount_taken
            most_taken_person = (i+1)
    return most_taken_person

def main():
    num_guests = 100
    result = largest_pie_guest(num_guests)
    print(f"Number of guests: {num_guests}")
    print(f"Largest piece goes to guest: {result}")

if __name__ == "__main__":
    main()