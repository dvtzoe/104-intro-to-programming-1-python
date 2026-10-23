def is_even(number: int) -> bool:
    return number % 2 == 0


def main() -> None:
    for i in range(1, 6):
        print(i, is_even(i))


if __name__ == "__main__":
    main()
