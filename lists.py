# add friends to list and then add their fav number to another list
# count it and count average
friends = list()
friends_fav_num = list()
while True:
    name = input("Enter your friend Name: ")
    if name == "done":
        break
    friends.append(name)
print(friends)

count = 0
while True:
    num_fav = input("Enter Friend Fav Number: ")
    if num_fav == "done":
        break
    num_f_int = float(num_fav)
    friends_fav_num.append(num_f_int)
    count = count + 1
average = sum(friends_fav_num) / count
print("Average:", average)

print("\n\n Splitting Words\n\n")

line = "From Kamran_hccp@icloud.com at Sat 03May 03:03:03 2023"
words = line.split()
print(words)

print(dir(friends))
