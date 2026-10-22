import sys

raw_age = input("Age: ")
raw_seat = input("Seat (normal/premium): ")
raw_weekend = input("Weekend? (yes/no)")
raw_student_card = input("Student card? (yes/no): ")

try:
    age = int(raw_age)
except ValueError:
    print("Please enter a valid age;")
    sys.exit()

if raw_seat == "normal":
    is_seat_normal = True
elif raw_seat == "premium":
    is_seat_normal = False
else:
    print("Unknown seat type")
    sys.exit()

if raw_weekend == "yes":
    is_weekend = True
elif raw_weekend == "no":
    is_weekend = False
else:
    print("Please enter only yes/no")
    sys.exit()

if raw_student_card == "yes":
    is_student_card = True
elif raw_student_card == "no":
    is_student_card = False
else:
    print("Please enter only yes/no")
    sys.exit()

if is_seat_normal:
    ticket_price = 220
else:
    ticket_price = 350

if age < 12 or age >= 60:
    ticket_price /= 2

if is_student_card and not is_weekend:
    ticket_price *= 0.8

if is_weekend:
    ticket_price += 30

print(f"Ticket price: {ticket_price} baht")
