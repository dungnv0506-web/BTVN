import sys
import sqlite3
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem
)

# ================= DATABASE =================
def connect_db():
    return sqlite3.connect("nhansu.db")

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS nhansu (
        cccd TEXT PRIMARY KEY,
        hoten TEXT,
        ngaysinh TEXT,
        gioitinh TEXT,
        diachi TEXT
    )
    """)
    conn.commit()
    conn.close()

# ================= GUI =================
class NhanSuApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quản lý nhân sự")
        self.resize(800, 500)

        create_table()
        self.init_ui()
        self.load_data()

    def init_ui(self):
        layout = QVBoxLayout()

        # Input
        self.cccd = QLineEdit()
        self.hoten = QLineEdit()
        self.ngaysinh = QLineEdit()
        self.gioitinh = QLineEdit()
        self.diachi = QLineEdit()

        layout.addWidget(QLabel("CCCD"))
        layout.addWidget(self.cccd)

        layout.addWidget(QLabel("Họ tên"))
        layout.addWidget(self.hoten)

        layout.addWidget(QLabel("Ngày sinh"))
        layout.addWidget(self.ngaysinh)

        layout.addWidget(QLabel("Giới tính"))
        layout.addWidget(self.gioitinh)

        layout.addWidget(QLabel("Địa chỉ"))
        layout.addWidget(self.diachi)

        # Buttons
        btn_layout = QHBoxLayout()

        self.btn_add = QPushButton("Thêm")
        self.btn_update = QPushButton("Sửa")
        self.btn_delete = QPushButton("Xóa")
        self.btn_search = QPushButton("Tìm kiếm")
        self.btn_show = QPushButton("Hiển thị")

        btn_layout.addWidget(self.btn_add)
        btn_layout.addWidget(self.btn_update)
        btn_layout.addWidget(self.btn_delete)
        btn_layout.addWidget(self.btn_search)
        btn_layout.addWidget(self.btn_show)

        layout.addLayout(btn_layout)

        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["CCCD", "Họ tên", "Ngày sinh", "Giới tính", "Địa chỉ"])

        layout.addWidget(self.table)

        self.setLayout(layout)

        # Events
        self.btn_add.clicked.connect(self.add_data)
        self.btn_update.clicked.connect(self.update_data)
        self.btn_delete.clicked.connect(self.delete_data)
        self.btn_search.clicked.connect(self.search_data)
        self.btn_show.clicked.connect(self.load_data)
        self.table.cellClicked.connect(self.fill_data)

    # ================= FUNCTIONS =================
    def add_data(self):
        conn = connect_db()
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO nhansu VALUES (?, ?, ?, ?, ?)", (
                self.cccd.text(),
                self.hoten.text(),
                self.ngaysinh.text(),
                self.gioitinh.text(),
                self.diachi.text()
            ))
            conn.commit()
        except:
            print("CCCD đã tồn tại")

        conn.close()
        self.load_data()

    def load_data(self):
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM nhansu")
        rows = cursor.fetchall()

        self.table.setRowCount(0)
        for row_idx, row_data in enumerate(rows):
            self.table.insertRow(row_idx)
            for col_idx, col_data in enumerate(row_data):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

        conn.close()

    def update_data(self):
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE nhansu
        SET hoten=?, ngaysinh=?, gioitinh=?, diachi=?
        WHERE cccd=?
        """, (
            self.hoten.text(),
            self.ngaysinh.text(),
            self.gioitinh.text(),
            self.diachi.text(),
            self.cccd.text()
        ))

        conn.commit()
        conn.close()
        self.load_data()

    def delete_data(self):
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM nhansu WHERE cccd=?", (self.cccd.text(),))

        conn.commit()
        conn.close()
        self.load_data()

    def search_data(self):
        conn = connect_db()
        cursor = conn.cursor()

        keyword = self.cccd.text()

        cursor.execute("""
        SELECT * FROM nhansu
        WHERE cccd LIKE ? OR hoten LIKE ? OR diachi LIKE ?
        """, (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%"))

        rows = cursor.fetchall()

        self.table.setRowCount(0)
        for row_idx, row_data in enumerate(rows):
            self.table.insertRow(row_idx)
            for col_idx, col_data in enumerate(row_data):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

        conn.close()

    def fill_data(self, row, column):
        self.cccd.setText(self.table.item(row, 0).text())
        self.hoten.setText(self.table.item(row, 1).text())
        self.ngaysinh.setText(self.table.item(row, 2).text())
        self.gioitinh.setText(self.table.item(row, 3).text())
        self.diachi.setText(self.table.item(row, 4).text())


# ================= RUN =================
app = QApplication(sys.argv)
window = NhanSuApp()
window.show()
sys.exit(app.exec())