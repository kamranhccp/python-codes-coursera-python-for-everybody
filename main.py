fruit = 'banana'
index = 0
# while index is less than length of fruit letters, it will iterate
while index < len(fruit):  # firstly, index is 0 which have letter b
    # letter at index 0 will be stored in letterS
    letterS = fruit[index]
    # will print index(which is 0 at first) and letter at that index stored in letterS Variable
    print(index, letterS)
    # index will than be 1 after adding 0 to 1 = 1
    index = index + 1
print("\nAll done")

print("\nUsing for Loop")
ind = 0
for letter in fruit:
    print(str(ind), letter)
    ind = ind + 1

# to count letters in a string
strings = "loriaseasaedadasasadas"
countOfLetter = 0
for letter in strings:
    if letter == 's':
        countOfLetter = countOfLetter + 1
print("Count of Letter s in String:", countOfLetter)

# slicing letters
print(len(strings))
print(strings[0:3])  # 0 upto 3 but not including 3
print(strings[9:13])
print(strings[:])
print(strings[10:])  # from 10 upto last
print(strings[:4])  # start(0) upt0 4 not including 4
print(len(fruit) * 7)
