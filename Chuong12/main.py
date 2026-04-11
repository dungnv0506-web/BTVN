from math_utils import cong, nhan, dien_tich_tron, chu_vi_hcn

def main():
    # Thử nghiệm phân số: 1/2 + 1/3
    ps1 = (1, 2)
    ps2 = (1, 3)
    ket_qua_cong = cong(ps1, ps2)
    print(f"Tổng phân số: {ps1[0]}/{ps1[1]} + {ps2[0]}/{ps2[1]} = {ket_qua_cong[0]}/{ket_qua_cong[1]}")

    # Thử nghiệm hình học
    r = 5
    print(f"Diện tích hình tròn bán kính {r}: {dien_tich_tron(r):.2f}")
    
    dai, rong = 10, 5
    print(f"Chu vi hình chữ nhật {dai}x{rong}: {chu_vi_hcn(dai, rong)}")

if __name__ == "__main__":
    main()