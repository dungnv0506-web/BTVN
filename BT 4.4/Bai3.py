_tuple = ('ab', 'b', 'e', 'c', 'd', 'e', 'ab')

temp = []
for x in _tuple:
    if x not in temp:
        temp.append(x)

_new_tuple = tuple(temp)

print(_new_tuple)