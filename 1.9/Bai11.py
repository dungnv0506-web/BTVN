_list = ['apple', 'hi', 'banana', 'cat', 'orange']

n = int(input("Nhập n: "))

result = [word for word in _list if len(word) > n]

print("Kết quả:", result)