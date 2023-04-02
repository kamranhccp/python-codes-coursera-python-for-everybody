sentence = input("Enter something you want to share: ")
words = sentence.split()
words_dic = dict()
count = 0

print("Words: ", words)
print("Counting the words...")

for word in words:
    words_dic[word] = words_dic.get(word, 0) + 1
print("Total Counts:", words_dic)
