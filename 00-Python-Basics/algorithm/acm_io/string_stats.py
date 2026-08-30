
text = input()

words = text.split()
letters = 0

for word in words:
    letters += len(word)

print(len(words))
print(letters)