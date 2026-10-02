danh_sach_sinh_vien=[
    {"ma_sv": "01","ho_ten" : "Phạm Tuấn Dương","lop":"14C1-CNTT","dtb":8.5,"trang_thai":"Đang học"},
    {"ma_sv": "02","ho_ten" : "Phạm Quang Huy","lop":"14C1-CNTT","dtb":10.0,"trang_thai":"Đang học"},
    {"ma_sv": "03","ho_ten" : "Nguyễn Văn A","lop":"14C2-CNTT","dtb":6.5,"trang_thai":"Đang học"},
    {"ma_sv": "04","ho_ten" : "Vũ Văn B","lop":"14C2-CNTT","dtb":2.5,"trang_thai":"Bảo Lưu"},
]
lich_su=[]
def hien_thi():
    print("\n" +"-"*65)
    print(f"{'Mã SV':<10}{'Họ tên':<50}{'Lop':<15}{'DTB':<10}{'Trang thai':<12}")
    print("-"*65)
    for sv in danh_sach_sinh_vien:
        print(f"{sv['ma_sv']:<10}{sv['ho_ten']:<50}{sv['lop']:<15}{sv['dtb']:<10.1f}{sv['trang_thai']:<12}")
    print("="*65)
def tim_sinh_vien_theo_ma(ma_sv):
    for sv in danh_sach_sinh_vien:
        if sv["ma_sv"] == ma_sv:
            return sv
    return None
def xem_sinh_vien_dang_hoc():
    sv_dang_hoc =[sv for sv in danh_sach_sinh_vien if sv["trang_thai"]=="Đang học"]
    if len(sv_dang_hoc)==0:
        print("->Hiện không có sinh viên nào theo học.")
        return
    print("\nDanh sách sinh viên đang học:")
    for sv in sv_dang_hoc:
        print(f"{sv['ma_sv']} - {sv['ho_ten']} - Lop :{sv['lop']} - DTB :{sv['dtb']:.1f} ")
def them_sinh_vien(ma_sv, ho_ten, lop, dtb):
    if tim_sinh_vien_theo_ma(ma_sv) is not None:
        print(f"->Ma sinh viên {ma_sv} đã tồn tại, không thể thêm.")
        return
    danh_sach_sinh_vien.append({
        "ma_sv": ma_sv,"ho_ten":ho_ten,
        "lop":lop, "dtb":dtb,"trang_thai":"Đang học"
    })
    print(f"-> Đã thêm sinh viên {ho_ten}({ma_sv}) thành công.")

def  cap_nhat_diem(ma_sv,dtb_moi):
    sv= tim_sinh_vien_theo_ma(ma_sv)
    if sv is None:
        print(f"->Không tìm thấy sinh viên có mã {ma_sv}")
        return
    diem_cu=sv["dtb"]
    sv["dtb"]=dtb_moi
    lich_su.append({
        "ma_sv":ma_sv,"ho_ten":sv["ho_ten"],
        "diem_cu" : diem_cu,"diem_moi":dtb_moi
    })
    print(f"->Đã cập nhật thêm cho sinh viên{sv['ho_ten']}:{diem_cu:.1f}->{dtb_moi}")

def xet_ket_qua(ma_sv):
    sv=tim_sinh_vien_theo_ma(ma_sv)
    if sv is None:
        print(f"->Không tìm thấy sinh viên có mã{ma_sv},")
        return
    if sv["dtb"]>=5.0:
        danh_gia="Đạt (Đủ điều kiện)"
    elif sv ["dtb"]>=4.0:
        danh_gia="Cảnh bảo học tập"
    else :
        danh_gia ="Buộc thôi học/Học lại"
    print(f"\n->Kết quả xét học tập cuối kỳ:")
    print(f"SV: {sv['ho_ten']} ({sv['ma_sv']})|DTB:{sv['dtb']:.1f}")
    print(f"Đánh giá:{danh_gia}")
def thong_ke_xep_loai():
    if len(danh_sach_sinh_vien)==0:
        print("->Hiện không có sinh viên nào trong danh sách.")
        return
    xuat_sac=gioi=kha=trung_binh=yeu=0
    for sv in danh_sach_sinh_vien:
        dtb=sv["dtb"]
        if dtb>=9.0: xuat_sac+=1
        elif dtb>=8.0:  gioi+=1
        elif dtb>=6.5:  kha+=1
        elif dtb>=5.0:  trung_binh+=1
        else: yeu+=1
    print("\n->Thống kê xếp loại sinh viên:")
    print(f" - Xuất sắc: {xuat_sac}")
    print(f" - Giỏi: {gioi}")
    print(f" - Khá: {kha}")
    print(f" - Trung bình: {trung_binh}")
    print(f" - Yếu: {yeu}")
    print(f"\n>>> Tổng số sinh viên: {len(danh_sach_sinh_vien)}")
def nhap_so_thuc(loi_nhac):
    while True:
        try:
            so_thuc=float(input(loi_nhac))
            if 0.0<=so_thuc<=10.0:
                return so_thuc
            print("->Điểm phải nằm trong khoảng 0.0 đến 10.0")
        except ValueError:
            print("-> Dữ liệu không hợp lệ, vui lòng nhập lại 1 số thực.")
def hien_thi_menu():
    print("\n=== MENU QUẢN LÝ SINH VIÊN ===")
    print("1. Hiển thị  danh sách tất cả các sinh viên")
    print("2. Xem danh sách sinh viên đang học")
    print("3. Thêm sinh viên mới")
    print("4. Cập nhật điểm trung bình của sinh viên")
    print("5. Xét kết quả học tập cuối kỳ của sinh viên")
    print("6. Thống kê xếp loại sinh viên")
    print("0. Thoát chương trình")
def chay_chuong_trinh():
    while True:
        hien_thi_menu()
        lua_chon=input("->Nhập lựa chọn của bạn (0-6): ")
        if lua_chon=="1":
            hien_thi()
        elif lua_chon=="2":
            xem_sinh_vien_dang_hoc()
        elif lua_chon=="3":
            ma_sv=input("->Nhập mã sinh viên: ")
            ho_ten=input("->Nhập họ tên sinh viên: ")
            lop=input("->Nhập lớp sinh viên: ")
            dtb=nhap_so_thuc("->Nhập điểm trung bình (0.0-10.0): ")
            them_sinh_vien(ma_sv,ho_ten,lop,dtb)
        elif lua_chon=="4":
            ma_sv=input("->Nhập mã sinh viên cần cập nhật điểm: ")
            dtb_moi=nhap_so_thuc("->Nhập điểm trung bình mới (0.0-10.0): ")
            cap_nhat_diem(ma_sv,dtb_moi)
        elif lua_chon=="5":
            ma_sv=input("->Nhập mã sinh viên cần xét kết quả học tập: ")
            xet_ket_qua(ma_sv)
        elif lua_chon=="6":
            thong_ke_xep_loai()
        elif lua_chon=="0":
            print("->Thoát chương trình.")
            break
        else:
            print("->Lựa chọn không hợp lệ, vui lòng chọn lại.")
if __name__=="__main__":
    chay_chuong_trinh()