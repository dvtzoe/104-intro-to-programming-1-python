# year = int(input("Year: "))


def check_if_leap(year: int) -> None:
    is_leap = False

    if year % 4 == 0:
        if year % 400 == 0:
            is_leap = True
        elif year % 100 == 0:
            is_leap = False
        else:
            is_leap = True

    print(f"{year} is {'' if is_leap else 'not '}a leap year")


check_if_leap(2024)
check_if_leap(1900)
check_if_leap(2000)
check_if_leap(2026)
