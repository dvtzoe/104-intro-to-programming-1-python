number = int(input("Number: "))
print(f"Divisors of {number}: ", end="")

pairs = []

for i in range(1, int(number ** (1 / 2)) + 1):
    if number % i == 0:
        print(i, end=" ")
        pairs.append(number // i)

for pair in pairs[::-1]:
    print(pair, end=" ")
