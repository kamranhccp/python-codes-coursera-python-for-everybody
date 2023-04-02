# 7.2 Write a program that prompts for a file name, then opens that file and
# reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines
# and compute the average of those values and produce an output as shown below.
# Do not use the sum() function or a variable named sum in your solution

usr_inp = input("Enter file name: ")
handle = open(usr_inp)
total = 0
count = 0
for lines in handle:
    if not lines.startswith("X-DSPAM-Confidence:"): continue
    word = lines.find('0')
    num = float(lines[word:])
    total = total + num
    count = count + 1
    average = total/count

print("Average spam confidence:", average)

