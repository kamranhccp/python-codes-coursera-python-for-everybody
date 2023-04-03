# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number
# of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the
# person who sent the mail. The program creates a Python dictionary that maps the sender's mail address
# to a count of the number of times they appear in the file. After the dictionary is produced, the program
# reads through the dictionary using a maximum loop to find the most prolific committer.
fhnad = input("Enter File name: ")
if len(fhnad) < 1:
    name = "mbox-short.txt"
handle = open(fhnad)

sender = dict()
for line in handle:
    if line.startswith('From: '):
        line = line.rstrip().split()
        word = line[1]
        sender[word] = sender.get(word, 0) + 1

largest_word = None
largest_count = None

for word, count in sender.items():
    if largest_count is None or count > largest_count:
        largest_word = word
        largest_count = count
print(largest_word, largest_count)
