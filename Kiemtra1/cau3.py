import  pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Kiemtra1/sanpham.csv")

tong_so_sp = len(df)
gia_tb = df["Gia"].mean()
ten_sp_max = df.loc[df["Gia"].idxmax(),"TenSP"]

print ("Tong so san pham:", tong_so_sp)
print ("Gia trung binh:", gia_tb)
print ("Ten san pham co gia cao nhat:", ten_sp_max)

plt.figure(figsize=(6,4))
plt.bar(df["TenSP"], df["SoLuong"], color="skyblue")
plt.title("Số lượng tồn kho từng sản phẩm")
plt.xlabel("TenSP")
plt.ylabel("SoLuong")
plt.savefig("Kiemtra1/bieu_do.png")
plt.show()

df_sap_het = df[df["SoLuong"] < 10]
df_sap_het.to_csv("Kiemtra1/canh_bao_hang.csv", index=False)
print("Da xuat file canh bao")