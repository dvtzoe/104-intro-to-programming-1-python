n = int(input("How many numbers? "))
sum = 0
for i in range(n):
    sum += float(input(f"Number {i + 1}: "))
print(f"Sum: {sum}")
print(f"Average: {sum / n}")
