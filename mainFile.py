import lists

number = 0

for x in range(4):
    number = number + 1
    print('variable: ' + str(number))
    print('loop count x: ' + str(x))

print(lists.names['employee2'])

lists.names.update({'employee4': 'baby weez'})

for name in lists.names:
    print(name + ': ' + lists.names[name])
