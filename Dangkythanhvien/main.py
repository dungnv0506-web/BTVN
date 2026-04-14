import sys
import re
from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox
from Dangkythanhvien import Ui_Dialog
from Database import *
from danhsach import DanhSach   # thêm dòng này

class MyApp(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        create_table()  # tạo bảng

        # ====== NGÀY SINH ======
        for i in range(1, 32):
            self.ui.comboBox.addItem(str(i))

        for i in range(1, 13):
            self.ui.comboBox_2.addItem(str(i))

        for i in range(1980, 2026):
            self.ui.comboBox_3.addItem(str(i))

        self.ui.pushButton.clicked.connect(self.dangky)

    # ====== KIỂM TRA MẬT KHẨU ======
    def kiemtra_matkhau(self, mk):
        return (len(mk) >= 8 and
                re.search("[a-z]", mk) and
                re.search("[A-Z]", mk) and
                re.search("[0-9]", mk) and
                re.search("[^a-zA-Z0-9]", mk))

    def dangky(self):
        ho = self.ui.textEdit.toPlainText().strip()
        ten = self.ui.textEdit_2.toPlainText().strip()
        sdt = self.ui.textEdit_3.toPlainText().strip()
        mk = self.ui.textEdit_4.toPlainText().strip()

        ngay = self.ui.comboBox.currentText()
        thang = self.ui.comboBox_2.currentText()
        nam = self.ui.comboBox_3.currentText()
        ngaysinh = f"{ngay}/{thang}/{nam}"

        gioitinh = ""
        if self.ui.radioButton.isChecked():
            gioitinh = "Nam"
        elif self.ui.radioButton_2.isChecked():
            gioitinh = "Nữ"

        # ====== VALIDATE ======
        if not ho or not ten or not sdt or not mk:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return

        if not gioitinh:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn giới tính!")
            return

        if not self.kiemtra_matkhau(mk):
            QMessageBox.warning(
                self,
                "Lỗi",
                "Mật khẩu phải ≥ 8 ký tự, có chữ hoa, chữ thường, số và ký tự đặc biệt!"
            )
            return

        if not self.ui.checkBox.isChecked():
            QMessageBox.warning(self, "Lỗi", "Bạn chưa đồng ý điều khoản!")
            return

        # ====== LƯU DATABASE ======
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO users (ho, ten, ngaysinh, sdt, matkhau, gioitinh)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (ho, ten, ngaysinh, sdt, mk, gioitinh))

        conn.commit()
        conn.close()

        QMessageBox.information(self, "OK", "Đăng ký thành công!")

        # ====== MỞ DANH SÁCH ======
        self.ds = DanhSach()
        self.ds.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())