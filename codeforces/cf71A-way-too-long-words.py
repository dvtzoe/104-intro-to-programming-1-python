n = int(input())
words = []

for i in range(n):
    current_word = input()
    if len(current_word) > 10:
        current_word = current_word[0] + str(len(current_word) - 2) + current_word[-1]
    words.append(current_word)

print(*words, sep="\n")
