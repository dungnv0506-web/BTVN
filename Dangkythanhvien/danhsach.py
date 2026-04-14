from PyQt6.QtWidgets import QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem
import sqlite3

class DanhSach(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Danh sách database")
        self.resize(700, 400)

        layout = QVBoxLayout()

        self.table = QTableWidget()
        layout.addWidget(self.table)

        self.setLayout(layout)

        self.load_data()

    def load_data(self):
        conn = sqlite3.connect("D:/Dangkythanhvien/users.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        data = cursor.fetchall()

        self.table.setRowCount(len(data))
        self.table.setColumnCount(7)

        headers = ["ID", "Họ", "Tên", "Ngày sinh", "SĐT", "Mật khẩu", "Giới tính"]
        self.table.setHorizontalHeaderLabels(headers)

        for i, row in enumerate(data):
            for j, val in enumerate(row):
                self.table.setItem(i, j, QTableWidgetItem(str(val)))

        conn.close()