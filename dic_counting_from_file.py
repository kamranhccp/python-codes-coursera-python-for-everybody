fhand = input("Enter file name: ")
handle = open(fhand)
fwords = dict()

# line is not a reserved word but a pneumonic word: understandable to human
for line in handle:
    words = line.split()
    for word in words:
        fwords[word] = fwords.get(word, 0) + 1

print("Count:", fwords)
