# getting file name and the splitting their words
# and then counting the word with the largest count

fhand = input("Enter file name: ")
handle = open(fhand)
fcount = dict()

# line is not a reserved word but a pneumonic word: understandable to human
for line in handle:
    words = line.split()
    for word in words:
        fcount[word] = fcount.get(word, 0) + 1
print("Full Details of DicCount: ", fcount, "\n\n")

largest_word = None
largest_count = None

for word,count in fcount.items():
    if largest_count is None or count > largest_count:
        largest_word = word
        largest_count = count

print("Largest word:", largest_word, ": And with Count =", largest_count)
