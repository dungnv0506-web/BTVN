# Bảng mã
code_dict = {
    'a': '!',
    'b': '@',
    'c': '#',
    'd': '$'
}

# Tạo bảng giải mã (đảo key-value)
decode_dict = {v: k for k, v in code_dict.items()}


# ===== Hàm mã hóa =====
def encode(text):
    result = ""
    for ch in text:
        if ch in code_dict:
            result += code_dict[ch]
        else:
            result += ch  # giữ nguyên nếu không có trong bảng mã
    return result


# ===== Hàm giải mã =====
def decode(text):
    result = ""
    for ch in text:
        if ch in decode_dict:
            result += decode_dict[ch]
        else:
            result += ch
    return result


# ===== Menu =====
while True:
    print("\n===== MENU =====")
    print("1. Mã hóa")
    print("2. Giải mã")
    print("0. Thoát")

    choice = input("Chọn: ")

    if choice == '1':
        text = input("Nhập văn bản: ").lower()
        print("Kết quả mã hóa:", encode(text))

    elif choice == '2':
        text = input("Nhập văn bản mã hóa: ")
        print("Kết quả giải mã:", decode(text))

    elif choice == '0':
        print("Thoát chương trình")
        break

    else:
        print("Chọn sai!")