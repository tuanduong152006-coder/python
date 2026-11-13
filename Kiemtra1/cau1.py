import copy
danh_sach_mau=[
    {"MaSP":"SP001","TenSP":"Bút bi Thiên Long","Gia":"3000","SoLuong":"150"},
    {"MaSP":"SP002","TenSP":"Vở học sinh 96 trang","Gia":"8000","SoLuong":"8"},
    {"MaSP":"SP003","TenSP":"Bút chì 2B","Gia":"2500","SoLuong":"200"},
]
def tao_san_pham(ma, ten, gia ,soluong):
    return{
        "MaSP": ma,
        "TenSP": ten,
        "Gia": float(gia),
        "SoLuong": int(soluong)
    }
def them_san_pham(danh_sach, ma, ten, gia, soluong):
    sp = tao_san_pham(ma, ten, gia, soluong)
    danh_sach.append(sp)

def tim_kiem_theo_ten(danh_sach, tu_khoa):
    ket_qua =[]
    tu_khoa_lower = tu_khoa.strip().lower()
    for sp in danh_sach:
        if tu_khoa_lower in sp["TenSP"].strip().lower():
            ket_qua.append(sp)
    return ket_qua
def tong_gia_tri_ton_kho(danh_sach):
    tong =  0.0
    for sp in danh_sach:
        gia = float(sp["Gia"])
        soluong = int(sp["SoLuong"])
        tong += gia * soluong
    return tong
def main():
    danh_sach = copy.deepcopy(danh_sach_mau)
    while True:
        print("\nMenu:")
        print("1. Thêm sản phẩm")
        print("2. Tìm kiếm sản phẩm theo tên")
        print("3. Tính tổng giá trị tồn kho")
        print("4. Thoát")
        lua_chon = input("Nhập lựa chọn của bạn (1-4): ")
        if lua_chon == "1":
            try:
                ma = input("Nhap ma san pham: ")
                ten = input("Nhap ten san pham: ")
                gia = input("Nhap gia san pham: ")
                soluong = input("Nhap so luong san pham: ")
                them_san_pham(danh_sach, ma, ten, gia, soluong)
                print("Da them san pham thanh cong")
            except ValueError:
                print("Gia va so luong phai la so. Vui long nhap lai")
        elif lua_chon == "2":
            tu_khoa = input("Nhap tu khoa tim kiem: ")
            ket_qua = tim_kiem_theo_ten(danh_sach, tu_khoa)
            print("Ket qua tim kiem:")
            for sp in ket_qua:
                print(f"-{sp['TenSP']}: {sp['Gia']} VND")
        elif lua_chon == "3":
            tong = tong_gia_tri_ton_kho(danh_sach)
            print(f"Tong gia tri ton kho: {tong} VND")
        elif lua_chon == "4":
            print("Thoat chuong trinh")
            break
        else:
            print("Lua chon khong hop le. Vui long nhap lai")
if __name__ == "__main__":
    main()