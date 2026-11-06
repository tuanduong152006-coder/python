import datetime
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import csdl_chi_tieu as db

DANH_SACH_DANH_MUC = ["An uong", "Mua sam", "Di chuyen", "Giai tri", "Hoa don", "Khac"]

class UngDungQuanLyChiTieu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quan ly Chi tieu Ca nhan")
        self.geometry("620x520")
        self.resizable(False, False)
        
        db.tao_bang_neu_chua_co()
        self.khoi_tao_giao_dien()
        self.tai_lai_danh_sach()

    def khoi_tao_giao_dien(self):
        # Khung nhập liệu
        khung_nhap = tk.Frame(self)
        khung_nhap.pack(pady=10, padx=10, fill="x")

        tk.Label(khung_nhap, text="Ngay (YYYY-MM-DD):").grid(row=0, column=0, sticky="w", pady=5)
        self.o_nhap_ngay = tk.Entry(khung_nhap, width=30)
        self.o_nhap_ngay.insert(0, datetime.date.today().strftime("%Y-%m-%d"))
        self.o_nhap_ngay.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Danh muc:").grid(row=1, column=0, sticky="w", pady=5)
        self.chon_danh_muc = ttk.Combobox(khung_nhap, values=DANH_SACH_DANH_MUC, width=27, state="readonly")
        self.chon_danh_muc.current(0)
        self.chon_danh_muc.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="So tien (VND):").grid(row=2, column=0, sticky="w", pady=5)
        self.o_nhap_so_tien = tk.Entry(khung_nhap, width=30)
        self.o_nhap_so_tien.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Ghi chu:").grid(row=3, column=0, sticky="w", pady=5)
        self.o_nhap_ghi_chu = tk.Entry(khung_nhap, width=30)
        self.o_nhap_ghi_chu.grid(row=3, column=1, padx=10, pady=5)

        tk.Button(khung_nhap, text="Them giao dich", command=self.xu_ly_them).grid(row=4, column=0, columnspan=2, pady=10)

        # Khung danh sách
        khung_danh_sach = tk.Frame(self)
        khung_danh_sach.pack(pady=5, padx=10, fill="both", expand=True)

        self.listbox_chi_tieu = tk.Listbox(khung_danh_sach, width=80, height=12)
        self.listbox_chi_tieu.pack(side="left", fill="both", expand=True)

        thanh_cuon = tk.Scrollbar(khung_danh_sach, orient="vertical", command=self.listbox_chi_tieu.yview)
        thanh_cuon.pack(side="right", fill="y")
        self.listbox_chi_tieu.config(yscrollcommand=thanh_cuon.set)

        # Khung nút chức năng
        khung_nut = tk.Frame(self)
        khung_nut.pack(pady=10)

        tk.Button(khung_nut, text="Xoa giao dich", command=self.xu_ly_xoa).grid(row=0, column=0, padx=10)
        tk.Button(khung_nut, text="Thong ke theo danh muc (Bieu do)", command=self.xu_ly_thong_ke).grid(row=0, column=1, padx=10)

    def tai_lai_danh_sach(self):
        self.listbox_chi_tieu.delete(0, tk.END)
        self.danh_sach_hien_tai = db.lay_toan_bo_giao_dich()
        for gd in self.danh_sach_hien_tai:
            id_gd, ngay, danh_muc, so_tien, ghi_chu = gd
            chuoi_hien_thi = f"{ngay} | [{danh_muc}] {so_tien:,.0f} VND - Ghi chu: {ghi_chu}"
            self.listbox_chi_tieu.insert(tk.END, chuoi_hien_thi)

    def xu_ly_them(self):
        ngay = self.o_nhap_ngay.get().strip()
        danh_muc = self.chon_danh_muc.get()
        so_tien_str = self.o_nhap_so_tien.get().strip()
        ghi_chu = self.o_nhap_ghi_chu.get().strip()

        if not ngay or not so_tien_str:
            messagebox.showerror("Loi", "Vui long nhap ngay va so tien.")
            return

        try:
            so_tien = float(so_tien_str)
            if so_tien <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Loi", "So tien phai la mot so duong hop le.")
            return

        db.them_giao_dich(ngay, danh_muc, so_tien, ghi_chu)
        self.o_nhap_so_tien.delete(0, tk.END)
        self.o_nhap_ghi_chu.delete(0, tk.END)
        self.tai_lai_danh_sach()
        messagebox.showinfo("Thanh cong", "Da them giao dich chi tieu!")

    def xu_ly_xoa(self):
        lua_chon = self.listbox_chi_tieu.curselection()
        if not lua_chon:
            messagebox.showerror("Loi", "Vui long chon giao dich de xoa.")
            return
        id_gd = self.danh_sach_hien_tai[lua_chon[0]][0]
        db.xoa_giao_dich(id_gd)
        self.tai_lai_danh_sach()

    def xu_ly_thong_ke(self):
        du_lieu = db.thong_ke_theo_danh_muc()
        if not du_lieu:
            messagebox.showinfo("Thong bao", "Chua co du lieu chi tieu de thong ke.")
            return

        cac_danh_muc = [dong[0] for dong in du_lieu]
        # Quy đổi đơn vị sang nghìn (chia cho 1000)
        tong_tien = [dong[1] / 1000 for dong in du_lieu]

        plt.figure(figsize=(7, 4.5))
        plt.bar(cac_danh_muc, tong_tien, color="mediumseagreen")
        plt.title("Tong chi tieu theo danh muc")
        plt.xlabel("Danh muc")
        plt.ylabel("So tien (Nghin VND)")  # Đổi nhãn thành nghìn VND
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    app = UngDungQuanLyChiTieu()
    app.mainloop()