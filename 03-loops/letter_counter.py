# count how many times each letter appears in a word

word = input("Type word that you whant to check:")


counts = {}
for letter in word:
    if letter in counts:
        counts[letter] += 1
    else:
        counts[letter] = 1
print(counts)


counts = {}
for letter in word:
    counts[letter] = word.count(letter)
print(counts)