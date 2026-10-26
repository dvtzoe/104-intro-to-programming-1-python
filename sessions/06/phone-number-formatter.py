def clean_number(text: str) -> str:
    return text.strip().replace("-", "").replace(" ", "")


def is_valid(number: str) -> bool:
    return len(number) == 10 and number[0] == "0"


def digit_sum(number: str) -> int:
    sum = 0
    for digit in number:
        sum += int(digit)
    return sum


phone_number = input("Phone number: ")

phone_number = clean_number(phone_number)

if is_valid(phone_number):
    print(f"Formatted: {phone_number[0:3]}-{phone_number[3:6]}-{phone_number[6:]}")
    print(f"Hidden: {phone_number[0:3]}-XXX-{phone_number[6:]}")
    print(f"Digit sum: {digit_sum(phone_number)}")
else:
    print("Invalid phone number")
