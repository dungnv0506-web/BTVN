import os

def quan_ly_tep():
    ten_file = "du_lieu_cua_toi.txt"

    print(f"--- Bước 1: Tạo và ghi nội dung vào '{ten_file}' ---")
    noi_dung_ghi = [
        "Xin chào, đây là tệp được tạo bằng Python.\n",
        "Dòng thứ hai: Chúc bạn học lập trình vui vẻ!\n",
        "Dòng thứ ba: Python thật là mạnh mẽ."
    ]
    
    with open(ten_file, 'w', encoding='utf-8') as f:
        f.writelines(noi_dung_ghi)
    print("=> Tạo tệp thành công!\n")

    print(f"--- Bước 2: Ghi thêm dữ liệu vào tệp ---")
    with open(ten_file, 'a', encoding='utf-8') as f:
        f.write("\nĐây là dòng được ghi thêm vào cuối tệp.")
    print("=> Đã ghi thêm dữ liệu.\n")

    print(f"--- Bước 3: Đọc nội dung từ '{ten_file}' ---")
    if os.path.exists(ten_file):
        with open(ten_file, 'r', encoding='utf-8') as f:
            noi_dung_doc = f.read()
            print("Nội dung tệp hiện tại:")
            print("-" * 30)
            print(noi_dung_doc)
            print("-" * 30)
    else:
        print("Lỗi: Không tìm thấy tệp!")

if __name__ == "__main__":
    quan_ly_tep()