names = dict()
names['Khalid'] = 2
names['Kamran'] = 3
names['Yasir'] = 5
names['Hassan'] = 8
print(names)

names['Khalid'] = 3
names['Khalid'] = 4
names['Yasir'] = 10
names['Yasir'] = 20
names['Yasir'] = 31
print(names)

friends = dict()
names_friends = ['kamran', 'yasir', 'khalid', 'khalid', 'yasir', 'hamza', 'hassan',
                 'yasir', 'basaly', 'talha', 'yasir', 'basaly', 'kamran', 'kamran']
print(type(names_friends))
print(type(friends))

for name in names_friends:
    friends[name] = friends.get(name, 0) + 1
print(friends)
