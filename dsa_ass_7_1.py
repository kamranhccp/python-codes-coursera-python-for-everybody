# 7.1 Write a program that prompts for a file name, then opens that file
# and reads through the file, and print the contents of the file in upper case.
# Use the file words.txt to produce the output below.
user_input = input("Enter file name: ")
fhand = open(user_input)
for line in fhand:
    line.upper()  # .upper() adds doubles lines and can be solved this using rstrip
    print(line)

print("\n\n Line Break \n\n")

user_inp = input("Enter file name: ")
handle = open(user_inp)
for line in handle:
    skipping = line.rstrip()
    lines_edited = skipping.upper()
    print(lines_edited)
