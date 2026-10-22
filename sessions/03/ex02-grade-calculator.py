score = int(input("Score: "))
grade = ""

if score < 0 or score > 100:
    print("Invalid score")
else:
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"

    print(f"Grade: {grade}")
