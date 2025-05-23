from flask import Flask, render_template, request, send_file, redirect, url_for, flash
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from hashlib import sha256
import os
import datetime

app = Flask(__name__)
app.secret_key = "supersecret"  # Để sử dụng flash messages

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def derive_key(password):
    # Tạo khóa AES 128-bit từ mật khẩu bằng sha256 và cắt 16 byte đầu
    return sha256(password.encode()).digest()[:16]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("file")
        password = request.form.get("password")
        action = request.form.get("action")

        if not file or not password or not action:
            flash("Vui lòng chọn file, nhập mật khẩu và chọn hành động.", "danger")
            return redirect(url_for("index"))

        key = derive_key(password)
        original_filename = file.filename
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        input_path = os.path.join(UPLOAD_FOLDER, f"{timestamp}_{original_filename}")
        file.save(input_path)

        with open(input_path, "rb") as f:
            data = f.read()

        try:
            if action == "encrypt":
                iv = os.urandom(16)
                cipher = AES.new(key, AES.MODE_CBC, iv)
                encrypted_data = iv + cipher.encrypt(pad(data, AES.block_size))
                output_filename = original_filename + ".enc"
                output_data = encrypted_data
            elif action == "decrypt":
                iv = data[:16]
                cipher = AES.new(key, AES.MODE_CBC, iv)
                decrypted_data = unpad(cipher.decrypt(data[16:]), AES.block_size)
                output_filename = original_filename.replace(".enc", "") + ".dec"
                output_data = decrypted_data
            else:
                flash("Hành động không hợp lệ.", "danger")
                return redirect(url_for("index"))
        except Exception as e:
            flash("Lỗi trong quá trình mã hóa/giải mã. Kiểm tra mật khẩu hoặc định dạng file.", "danger")
            return redirect(url_for("index"))

        output_path = os.path.join(UPLOAD_FOLDER, f"{timestamp}_{output_filename}")
        with open(output_path, "wb") as f:
            f.write(output_data)

        # Trả file về trình duyệt để tải về
        return send_file(output_path, as_attachment=True)

    return render_template("index.html")
