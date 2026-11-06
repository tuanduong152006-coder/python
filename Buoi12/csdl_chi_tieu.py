import os
import sqlite3

THU_MUC_HIEN_TAI = os.path.dirname(os.path.abspath(__file__))
TEN_FILE_CSDL = os.path.join(THU_MUC_HIEN_TAI, "chi_tieu.db")

def ket_noi_csdl():
    return sqlite3.connect(TEN_FILE_CSDL)

def tao_bang_neu_chua_co():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("""
        CREATE TABLE IF NOT EXISTS chi_tieu (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ngay TEXT NOT NULL,
            danh_muc TEXT NOT NULL,
            so_tien REAL NOT NULL,
            ghi_chu TEXT
        )
    """)
    ket_noi.commit()
    ket_noi.close()

def them_giao_dich(ngay, danh_muc, so_tien, ghi_chu):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute(
        "INSERT INTO chi_tieu (ngay, danh_muc, so_tien, ghi_chu) VALUES (?, ?, ?, ?)",
        (ngay, danh_muc, so_tien, ghi_chu)
    )
    ket_noi.commit()
    ket_noi.close()

def lay_toan_bo_giao_dich():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("SELECT id, ngay, danh_muc, so_tien, ghi_chu FROM chi_tieu ORDER BY ngay DESC, id DESC")
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua

def xoa_giao_dich(id_giao_dich):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("DELETE FROM chi_tieu WHERE id = ?", (id_giao_dich,))
    ket_noi.commit()
    ket_noi.close()

def thong_ke_theo_danh_muc():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("SELECT danh_muc, SUM(so_tien) FROM chi_tieu GROUP BY danh_muc")
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua