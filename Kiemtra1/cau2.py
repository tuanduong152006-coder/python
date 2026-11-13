import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

class QuanLySanPham(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quan ly san pham")
        self.geometry("560x580")
        self.resizable(False, False)
        self.danh_sach_hien_tai = [
            ("SP001", "Bút bi Thiên Long", 3000, 150),
            ("SP002", "Vở học sinh 96 trang", 8000, 8),
            ("SP003", "Bút chì 2B", 2500, 200)
        ]

        self.khoi_tao_giao_dien()
        self.tai_lai_danh_sach()
    
    def khoi_tao_giao_dien(self):
        khung_nhap = tk.Frame(self)
        khung_nhap.pack(pady=10, padx=10, fill="x")
        
        tk.Label(khung_nhap, text="Ma san pham: ").grid(row=0, column=0, sticky="w", pady=5)
        self.o_nhap_ma_san_pham = tk.Entry(khung_nhap, width=30)
        self.o_nhap_ma_san_pham.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(khung_nhap, text="Ten san pham: ").grid(row=1, column=0, sticky="w", pady=5)
        self.o_nhap_ten_san_pham = tk.Entry(khung_nhap, width=30)
        self.o_nhap_ten_san_pham.grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(khung_nhap, text="Gia:").grid(row=2, column=0, sticky="w", pady=5)
        self.o_nhap_gia = tk.Entry(khung_nhap, width=30)
        self.o_nhap_gia.grid(row=2, column=1, padx=10, pady=5)
        
        tk.Label(khung_nhap, text="So Luong: ").grid(row=3, column=0, sticky="w", pady=5)
        self.o_nhap_so_luong = tk.Entry(khung_nhap, width=30)
        self.o_nhap_so_luong.grid(row=3, column=1, padx=10, pady=5)

        tk.Button(khung_nhap, text="Them san pham", command=self.xu_ly_them_san_pham, bg="#4CAF50", fg="white").grid(row=4, column=0, columnspan=2, pady=10)
        khung_danh_sach = tk.Frame(self)
        khung_danh_sach.pack(pady=5, padx=10, fill="both", expand=True)
        
        self.listbox_sach = tk.Listbox(khung_danh_sach, width=75, height=14)
        self.listbox_sach.pack(side="left", fill="both", expand=True)

        thanh_cuon = tk.Scrollbar(khung_danh_sach, orient="vertical", command=self.listbox_sach.yview)
        thanh_cuon.pack(side="right", fill="y")
        self.listbox_sach.config(yscrollcommand=thanh_cuon.set)
        khung_nut = tk.Frame(self)
        khung_nut.pack(pady=10)

        tk.Button(khung_nut, text="Tim kiem san pham", command=self.xu_ly_tim_kiem).grid(row=0, column=0, padx=5)
        tk.Button(khung_nut, text="Xoa san pham", command=self.xu_ly_xoa_sach).grid(row=0, column=1, padx=5)
        tk.Button(khung_nut, text="Hien thi tat ca", command=self.tai_lai_danh_sach).grid(row=0, column=2, padx=5)

    def tai_lai_danh_sach(self):
        self.listbox_sach.delete(0, tk.END)
        for sp in self.danh_sach_hien_tai:
            ma_sp, ten_sp, gia, so_luong = sp
            hien_thi = f"{ma_sp} - {ten_sp} - {gia:,.0f}đ - SL: {so_luong}"
            self.listbox_sach.insert(tk.END, hien_thi)

    def xu_ly_them_san_pham(self):
        ma = self.o_nhap_ma_san_pham.get().strip()
        ten = self.o_nhap_ten_san_pham.get().strip()
        str_gia = self.o_nhap_gia.get().strip()
        str_sl = self.o_nhap_so_luong.get().strip()

        if not ma or not ten:
            messagebox.showerror("Lỗi", "Mã và Tên sản phẩm không được để trống!")
            return
        
        try:
            gia = float(str_gia)
            so_luong = int(str_sl)
            if gia < 0 or so_luong < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Lỗi", "Giá phải là số và Số lượng phải là số nguyên không âm!")
            return

        self.danh_sach_hien_tai.append((ma, ten, gia, so_luong))
        self.tai_lai_danh_sach()
        
        self.o_nhap_ma_san_pham.delete(0, tk.END)
        self.o_nhap_ten_san_pham.delete(0, tk.END)
        self.o_nhap_gia.delete(0, tk.END)
        self.o_nhap_so_luong.delete(0, tk.END)
        messagebox.showinfo("Thành công", "Đã thêm sản phẩm thành công!")

    def xu_ly_tim_kiem(self):
        tu_khoa = self.o_nhap_ten_san_pham.get().strip().lower()
        if not tu_khoa:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập tên sản phẩm cần tìm vào ô Tên sản phẩm!")
            return
        
        ket_qua = [sp for sp in self.danh_sach_hien_tai if tu_khoa in sp[1].lower()]
        self.listbox_sach.delete(0, tk.END)
        for sp in ket_qua:
            ma_sp, ten_sp, gia, so_luong = sp
            hien_thi = f"{ma_sp} - {ten_sp} - {gia:,.0f}đ - SL: {so_luong}"
            self.listbox_sach.insert(tk.END, hien_thi)

    def xu_ly_xoa_sach(self):
        selection = self.listbox_sach.curselection()
        if not selection:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn sản phẩm cần xóa trong danh sách!")
            return
        
        index = selection[0]
        sp_bi_xoa = self.danh_sach_hien_tai.pop(index)
        self.tai_lai_danh_sach()
        messagebox.showinfo("Thành công", f"Đã xóa sản phẩm: {sp_bi_xoa[1]}")

if __name__ == "__main__":
    app = QuanLySanPham()
    app.mainloop()