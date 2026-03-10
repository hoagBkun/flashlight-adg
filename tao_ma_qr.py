import qrcode

def tao_qr_code_chua_link(duong_link, ten_file):
    try:
        # Thiết lập các thông số cho QR Code
        qr = qrcode.QRCode(
            version=1,  # Số 1 là nhỏ nhất, thư viện sẽ tự động tăng kích thước nếu link quá dài
            error_correction=qrcode.constants.ERROR_CORRECT_H, # Mức độ sửa lỗi CAO NHẤT (30%)
            box_size=10, # Độ phân giải (Kích thước của mỗi ô vuông nhỏ)
            border=4,    # Viền trắng an toàn xung quanh (Quiet Zone)
        )
        
        # Nhúng đường link vào QR Code
        qr.add_data(duong_link)
        qr.make(fit=True)

        # Tạo hình ảnh QR màu đen, nền trắng
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Lưu thành file PNG
        img.save(f"{ten_file}.png")
        
        print("-" * 40)
        print("✅ ĐÃ TẠO QR CODE THÀNH CÔNG!")
        print(f"📍 Tên file: {ten_file}.png")
        print(f"🔗 Đường link đã nhúng: {duong_link}")
        print("-" * 40)
        
    except Exception as e:
        print(f"❌ Có lỗi xảy ra: {e}")

# --- CHẠY THỬ ---
if __name__ == "__main__":
    # Thay đường link của bạn vào đây
    link_cua_ban = "https://hoagbkun.github.io/flashlight-adg/"
    
    # Đặt tên file (không cần ghi đuôi .png)
    ten_file_anh = "qr_den_pin_MH503"
    
    tao_qr_code_chua_link(link_cua_ban, ten_file_anh)