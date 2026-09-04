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