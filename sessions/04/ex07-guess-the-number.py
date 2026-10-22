import random

answer = random.randint(1, 100)

attempts = 0

while True:
    guess = int(input("Your guess (1-100): "))
    attempts += 1

    if guess == answer:
        print(f"Correct! You needed {attempts} attempts.")
        break
    elif guess > answer:
        print("Lower!")
    elif guess < answer:
        print("Higher!")
