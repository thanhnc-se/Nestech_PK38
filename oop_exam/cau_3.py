# Xử lý ngoại lệ là một phần quan trọng trong lập trình
# vì nó giúp ta quản lý và xử lý các lỗi xảy ra trong quá trình thực thi chương trình
# mà không làm cho chương trình bị dừng đột ngột.
# Điều này giúp cải thiện độ tin cậy và tính ổn định của ứng dụng.

# try:
#     # Khối lệnh có thể gây ra ngoại lệ
#     # Đây là khối lệnh chính mà ta muốn theo dõi để xử lý ngoại lệ.
#     # Bất kỳ lệnh nào có khả năng gây ra ngoại lệ đều nên được đặt trong khối này.
#     pass
# except Exception as e:
#     # Khối lệnh xử lý ngoại lệ nếu nó xảy ra trong khối try
#     # Khối này sẽ xử lý ngoại lệ nếu nó xảy ra trong khối try.
#     # ta có thể chỉ định cụ thể loại ngoại lệ cần bắt và xử lý,
#     # hoặc có thể dùng except mà không chỉ định loại ngoại lệ để bắt tất cả các loại ngoại lệ.
#     pass
# else:
#     # Khối lệnh này được thực thi nếu không có ngoại lệ xảy ra trong khối try
#     # Khối này chỉ được thực thi nếu không có ngoại lệ nào xảy ra trong khối try.
#     # Nó thường được sử dụng để thực hiện các lệnh cần thiết sau khi các lệnh trong khối try thành công.
#     pass
# finally:
#     # Khối lệnh này luôn được thực thi, bất kể có xảy ra ngoại lệ hay không
#     # Khối này luôn được thực thi, bất kể có xảy ra ngoại lệ hay không.
#     # Nó thường được sử dụng để dọn dẹp tài nguyên, đóng tệp, hoặc thực hiện các tác vụ dọn dẹp khác.
#     pass


try:
    # Mở tệp để đọc
    f = open("oop_exam/file.txt", "r")
    content = f.read()
    print(content)
except FileNotFoundError as e:
    # Xử lý ngoại lệ tệp không tìm thấy
    print("Error: File not found")
except IOError as e:
    # Xử lý các lỗi I/O khác
    print("Error: An I/O error occurred")
else:
    # Thực hiện nếu không có lỗi
    print("File read successfully")
finally:
    # Đảm bảo rằng tệp luôn được đóng
    try:
        f.close()
    except NameError:
        pass  # Nếu f chưa được định nghĩa do lỗi xảy ra trước khi mở tệp


# Viết code nhập 1 số từ bàn phím, in ra bình phương của số
# Xử lý ngoại lệ với lỗi ko chuyển được sang kiểu số
