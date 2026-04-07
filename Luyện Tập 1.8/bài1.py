# Bài 1
_tuple = ('a', 'b', 'd', 'e')

# thêm 'c' vào vị trí index 2
_new_tuple = _tuple[:2] + ('c',) + _tuple[2:]

print("Tuple mới:", _new_tuple)