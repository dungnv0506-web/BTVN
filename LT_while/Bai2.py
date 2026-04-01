n = int(input("Nhập n: "))
i = 1
gt = 1

while i <= n:
    gt *= i
    i += 1

print("Giai thừa =", gt)