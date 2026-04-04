# ================== FILE IO PROJECT ==================

# ===== BÀI 1: ĐỌC N DÒNG ĐẦU =====
def doc_n_dong():
    filename = "data.txt"
    try:
        n = int(input("Nhập số dòng cần đọc: "))
        with open(filename, "r", encoding="utf-8") as f:
            print("\n📄 Nội dung:")
            for i in range(n):
                line = f.readline()
                if not line:
                    break
                print(line.strip())
    except FileNotFoundError:
        print("❌ Không tìm thấy file data.txt")

# ===== BÀI 2: GHI VÀ ĐỌC FILE =====
def ghi_va_doc():
    filename = "vanban.txt"
    text = input("Nhập nội dung cần ghi: ")

    # Ghi file
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)

    # Đọc lại
    print("\n📄 Nội dung vừa ghi:")
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())

# ===== BÀI 3: TẠO FILE + ĐỌC =====
def tao_file_demo():
    filename = "demo_file1.txt"

    # Tạo file
    with open(filename, "w", encoding="utf-8") as f:
        f.write("Thuc\nhanh\nvoi\nfile\nIO")

    print("✅ Đã tạo file demo_file1.txt")

def in_1_dong():
    try:
        with open("demo_file1.txt", "r", encoding="utf-8") as f:
            content = f.read()
            print("\n📄 In trên 1 dòng:")
            print(content.replace("\n", " "))
    except:
        print("❌ Chưa tạo file!")

def in_tung_dong():
    try:
        with open("demo_file1.txt", "r", encoding="utf-8") as f:
            print("\n📄 In từng dòng:")
            for line in f:
                print(line.strip())
    except:
        print("❌ Chưa tạo file!")

# ================== MENU ==================
while True:
    print("\n========== MENU FILE ==========")
    print("1. Đọc n dòng đầu (data.txt)")
    print("2. Ghi và đọc file (vanban.txt)")
    print("3. Tạo file demo")
    print("4. In nội dung file trên 1 dòng")
    print("5. In nội dung file từng dòng")
    print("0. Thoát")

    chon = input("Chọn chức năng: ")

    if chon == "1":
        doc_n_dong()
    elif chon == "2":
        ghi_va_doc()
    elif chon == "3":
        tao_file_demo()
    elif chon == "4":
        in_1_dong()
    elif chon == "5":
        in_tung_dong()
    elif chon == "0":
        print("👋 Thoát chương trình")
        break
    else:
        print("❌ Chọn sai!")