1.)Giới thiệu code
Đây là một giao diện web viết bằng HTML kết hợp với Bootstrap, cho phép người dùng tải lên một file và nhập mật khẩu để thực hiện thao tác mã hóa (encrypt) hoặc giải mã (decrypt) file bằng thuật toán AES (Advanced Encryption Standard).

Tuy nhiên, đoạn mã HTML này chỉ xây dựng giao diện (frontend). Để hoạt động đầy đủ, nó cần một phần backend (ví dụ: PHP, Python, Node.js...) xử lý việc mã hóa/giải mã thực tế khi người dùng gửi biểu mẫu.
2.)Chức năng cơ bản của code
Giao diện đơn giản và thân thiện với người dùng:

Hiển thị trong một thẻ card của Bootstrap, giúp giao diện đẹp và rõ ràng.

Có hỗ trợ responsive (hiển thị tốt trên mọi thiết bị).

Chọn file cần mã hóa/giải mã:

Sử dụng <input type="file"> để người dùng tải file lên từ máy tính.

Nhập mật khẩu:

Dùng <input type="password"> để người dùng nhập mật khẩu dùng cho AES.

Hai nút chức năng:

Mã hóa (Encrypt): gửi biểu mẫu với giá trị action="encrypt".
Giải mã (Decrypt): gửi biểu mẫu với giá trị action="decrypt".
Để hoàn thiện ứng dụng, bạn cần:

Viết backend xử lý mã hóa/giải mã AES, ví dụ:

PHP: dùng thư viện openssl_encrypt / openssl_decrypt.

Python: dùng pycryptodome hoặc cryptography.

Node.js: dùng crypto module.

Bổ sung xử lý lỗi, thông báo thành công/thất bại, hiển thị thông tin file đã xử lý.
