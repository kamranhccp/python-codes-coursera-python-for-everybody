# 8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words
# using the split() method. The program should build a list of words. For each word on each line check
# to see if the word is already in the list and if not append it to the list. When the program completes,
# sort and print the resulting words in python sort() order as shown in the desired output.

fname = input("Enter file name: ")
file_romeo = open(fname)
romeo_list = list()                       # list for the desired output
for line in file_romeo:                    # to read every line of file romeo.txt
    words_all = line.rstrip().split()    # to eliminate the unwanted blanks and turn the line into a list of words
    for word in words_all:           # check every element in word
        if word in romeo_list:         # if element is repeated
            continue               # do nothing
        else:                     # else if element is not in the list
            romeo_list.append(word)    # append
romeo_list.sort()                         # sort the list (de-indent indicates that you sort when the loop ends)
print (romeo_list)

fname = input("Enter file name: ")
file_romeo = open(fname)
romeo_list = list()

for line in file_romeo:
    words_all = line.rstrip().split()
    for word in words_all:
        if word in romeo_list:
            continue
        else:
            romeo_list.append(word)

romeo_list.sort()
print(romeo_list)
