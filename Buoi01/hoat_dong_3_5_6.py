"""
3.1
Định Danh	 Trạng Thái	Lý do
1diem	     Sai	    Bắt đầu bằng số
gia-tri	     Sai	    Chứa dấu gạch ngang -
_tam_thoi	 Hợp Lệ	
Diem_TB	     Hợp Lệ	
class	     Sai	    Trùng với khóa hệ thống
so luong     Sai        Chứa khoảng trắng
MAX_SPEED	 Hợp Lệ	
diemTB	     Hợp Lệ	
2024_data	 Sai	    Bắt đầu bằng số
tong$	     Sai	    Có ký tự đặc biệt $
sinhVien1	 Hợp Lệ	
"""
ten = "Nguyen Van A"
diem_toan = 8.5
diem_van = 7.0
so_luong_mon_hoc = 2
MUC_LUONG_TOI_THIEU = 5000000

print("Họ tên:", ten)
print("Điểm Toán:", diem_toan)
print("Điểm Văn:", diem_van)
print("Số lượng môn học:", so_luong_mon_hoc)
print("Mức lương tối thiểu:", MUC_LUONG_TOI_THIEU)


a = 17
b = 5

print("a + b =", a + b)   
print("a - b =", a - b)  
print("a * b =", a * b)   
print("a / b =", a / b) 
print("a // b =", a // b) 
print("a % b =", a % b)  
print("a ** b =", a ** b) 
"""
Phân biệt giữa / và //:
/  : Luôn trả về kết quả kiểu số thực (float), kể cả khi chia hết (ví dụ: 17 / 5 cho ra 3.4).
// : Thực hiện chia và làm tròn xuống số nguyên gần nhất, trả về phần nguyên của kết quả (ví dụ: 17 // 5 cho ra 3).
Phân biệt giữa % và //:
% (Phép chia lấy phần dư): Trả về thương số dư còn lại sau phép chia nguyên (ví dụ: 17 % 5 cho ra 2).
// (Phép chia lấy phần nguyên): Trả về phần nguyên của thương (ví dụ: 17 // 5 cho ra 3).
"""

diem = 6.5
tuoi = 20
if ( diem >= 6.5 and diem < 8.0):
    print("diem dat loai kha")
    
if ( tuoi < 18 or tuoi > 60):
    print("tuoi khong hop le")
    
if not ( tuoi < 18 or tuoi > 60):
    print("tuoi hop le")

x = 10
x += 5;  print("x += 5  ->", x)  
x -= 3;  print("x -= 3  ->", x)  
x *= 2;  print("x *= 2  ->", x)  
x /= 4;  print("x /= 4  ->", x)   
x //= 2; print("x //= 2 ->", x)  
x **= 3; print("x **= 3 ->", x) 

danh_sach = [1, 2, 3, "python"]
print("3 co trong danh sach?:", 3 in danh_sach)

list_a = [1, 2, 3]
list_b = list_a
print("list_a is list_b?:", list_a is list_b)

print(2 + 3 * 4 ** 2)
print((2 + 3) * 4 ** 2)
print(10 > 5 and 3 < 1 or not False)
"""Ket qua du doan :  print(2 + 3 * 4 ** 2) : do uu tien se la **, *, +, => 2 + 3 * 16 = 2 + 48 = 50
Ket qua du doan :  print((2 + 3) * 4 ** 2) : do uu tien se la (), **, *,  => (5) * 16 = 80
Ket qua du doan :  print(10 > 5 and 3 < 1 or not False) : do uu tien se la and, or, not => (True and False) or True = False or True = True"""

bien = 10
print(bien, type(bien))

bien = "Xin chao"
print(bien, type(bien))

bien = 3.14
print(bien, type(bien))

bien = True
print(bien, type(bien))
"""Tại sao bien đổi được nhiều kiểu? Python dùng cơ chế Dynamic Typing (kiểu dữ liệu động). Bản chất tên biến chỉ là cái "nhãn" trỏ 
đến ô nhớ. Kiểu dữ liệu nằm ở giá trị, không nằm ở tên biến. Khi gán giá trị mới, nhãn chỉ việc chuyển sang trỏ vào giá trị mới đó.

Khác gì so với C/C++/Java? Các ngôn ngữ đó dùng Static Typing (kiểu dữ liệu tĩnh). Ngay khi khai báo int bien = 10;, ô nhớ bị khóa
 chặt cho kiểu số nguyên (int). Bác gán chuỗi hay số thực vào là chương trình báo lỗi ngay lập tức."""


ho_ten = "Nguyen Van A"
diem_toan = 8.0
diem_ly = 7.5
diem_hoa = 9.0

dtb = (diem_toan + diem_ly + diem_hoa) / 3

la_gioi = dtb >= 8.0
la_kha = dtb >= 6.5 and dtb < 8.0
la_trung_binh = dtb >= 5.0 and dtb < 6.5
la_yeu = dtb < 5.0

print(ho_ten, "- DTB:", round(dtb, 2))
print("Dat loai Gioi?", la_gioi)
print("Dat loai Kha?", la_kha)
print("Dat loai Trung binh?", la_trung_binh)
print("Dat loai Yeu?", la_yeu)
print("Kieu du lieu cua la_gioi:", type(la_gioi))