import tkinter as tk
from tkinter import messagebox

def nhap(gia_tri):
    hien_tai = bien_mh.get()
    if hien_tai == "0":
        bien_mh.set(gia_tri)
    else:
        bien_mh.set(hien_tai + gia_tri)

def xoa():
    bien_mh.set("0")

def tinh():
    try:
        ket_qua = eval(bien_mh.get())
        bien_mh.set(str(ket_qua))
    except:
        messagebox.showerror("Loi", "bieu thuc khong hop le")
        bien_mh.set("0")

cua_so = tk.Tk()
cua_so.title("may tinh don gian")
cua_so.geometry("260x340")
cua_so.resizable(False, False)

bien_mh = tk.StringVar(value="0")

man_hinh = tk.Entry(cua_so, textvariable=bien_mh, font=("Arial", 18), justify="right")
man_hinh.grid(row=0, column=0, columnspan=4, padx=5, pady=10, ipady=8, sticky="we")

nut_bam = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]
for (text, r, c) in nut_bam:
    if text == '=':
        btn = tk.Button(cua_so, text=text, font=("Arial", 14), bg="#4CAF50", fg="white", command=tinh)
    else:
        btn = tk.Button(cua_so, text=text, font=("Arial", 14), command=lambda t=text: nhap(t))
    btn.grid(row=r, column=c, padx=3, pady=3, sticky="nsew")
btn_xoa = tk.Button(cua_so, text="C", font=("Arial", 14), bg="#f44336", fg="white", command=xoa)
btn_xoa.grid(row=5, column=0, columnspan=4, padx=3, pady=3, sticky="we")
for i in range(6):
    cua_so.grid_rowconfigure(i, weight=1)
for j in range(4):
    cua_so.grid_columnconfigure(j, weight=1)

cua_so.mainloop()