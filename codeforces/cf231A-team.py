n = int(input())

problems_count = 0

for i in range(n):
    knows = input().split()
    if knows.count("1") >= 2:
        problems_count += 1

print(problems_count)
