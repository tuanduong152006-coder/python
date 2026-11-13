import csdl_sach as db

def chay_kiem_thu():
    db.tao_bang_neu_chua_co()
    print("--- 1. Them 2 cuon sach ---")
    db.them_sach("Nha Gia Kim", "Paulo Coelho", "Tieu thuyet")
    db.them_sach("Sapiens", "Yuval Noah Harari", "Lich su")
    danh_sach = db.lay_toan_bo_sach()
    print("Danh sach sau khi them 2 cuon:")
    for sach in danh_sach:
        print(sach)
    print("\n--- 2. Danh dau da doc cuon dau tien ---")
    db.danh_dau_da_doc(1)
    danh_sach = db.lay_toan_bo_sach()
    print("Sau khi danh dau da doc cuon dau tien:")
    for sach in danh_sach:
        print(sach)
    print("\n--- 3. Xoa cuon thu hai ---")
    db.xoa_sach(2)
    danh_sach = db.lay_toan_bo_sach()
    print("Sau khi xoa cuon thu hai:")
    for sach in danh_sach:
        print(sach)
if __name__ == "__main__":
    chay_kiem_thu()