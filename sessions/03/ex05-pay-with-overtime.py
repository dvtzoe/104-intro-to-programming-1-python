try:
    hours = int(input("Enter hours: "))
    rate = int(input("Enter rate: "))

    if hours > 40:
        pay = (40 + (hours - 40) * 1.5) * rate
    else:
        pay = hours * rate

    print(f"Pay: {pay}")
except ValueError:
    print("Error, please enter numeric input")
