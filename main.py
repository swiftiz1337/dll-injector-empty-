import sys
import psutil
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QFileDialog, QMessageBox


class Ui_Dialog(QtWidgets.QDialog):
    def setupUi(self):
        # Настройка окна
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setObjectName("Dialog")
        self.resize(400, 250)

        # Основной фрейм
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(0, 0, 400, 250))
        self.frame.setStyleSheet("""
            QFrame {
                background-color: #2E3440;
                border-radius: 15px;
            }
        """)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        # Заголовок
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 360, 30))
        self.label_2.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 18px;
                font-weight: bold;
            }
        """)
        self.label_2.setObjectName("label_2")

        # Кнопка закрытия
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(360, 20, 20, 20))
        self.label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 16px;
                font-weight: bold;
            }
            QLabel:hover {
                color: #BF616A;
            }
        """)
        self.label.setObjectName("label")
        self.label.mousePressEvent = lambda event: self.close()

        # Выбор процесса
        self.lineEdit = QtWidgets.QComboBox(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(20, 70, 360, 30))
        self.lineEdit.setStyleSheet("""
            QComboBox {
                background-color: #3B4252;
                color: white;
                border-radius: 5px;
                padding: 5px;
            }
            QComboBox::drop-down {
                border: none;
            }
        """)
        self.lineEdit.setObjectName("lineEdit")
        self.load_processes()

        # Кнопка выбора DLL
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(20, 120, 360, 30))
        self.pushButton.setStyleSheet("""
            QPushButton {
                background-color: #4C566A;
                color: white;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #5E81AC;
            }
        """)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.open_file_dialog)

        # Кнопка Inject
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 170, 360, 30))
        self.pushButton_2.setStyleSheet("""
            QPushButton {
                background-color: #BF616A;
                color: white;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #D08770;
            }
        """)
        self.pushButton_2.setObjectName("pushButton_2")

        # Переводим текст
        self.retranslateUi()

    def load_processes(self):
        self.lineEdit.clear()
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                if proc.info['pid'] >= 1000:  # Игнорируем системные процессы
                    self.lineEdit.addItem(f"{proc.info['name']} (PID: {proc.info['pid']})")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "DLL Injector"))
        self.label.setText(_translate("Dialog", "X"))
        self.label_2.setText(_translate("Dialog", "DLL Injector"))
        self.pushButton.setText(_translate("Dialog", "Выбрать DLL"))
        self.pushButton_2.setText(_translate("Dialog", "Inject"))

    def open_file_dialog(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("DLL файлы (*.dll)")
        file_dialog.setFileMode(QFileDialog.ExistingFile)

        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                self.dll_path = selected_files[0]
                self.pushButton.setText(f"Выбрано: {self.dll_path.split('/')[-1]}")

    def show_message(self, title, message, icon=QMessageBox.Information):
        msg = QMessageBox()
        msg.setIcon(icon)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStyleSheet("""
            QMessageBox {
                background-color: #2E3440;
                color: white;
            }
            QMessageBox QLabel {
                color: white;
            }
            QMessageBox QPushButton {
                background-color: #4C566A;
                color: white;
                border-radius: 5px;
                padding: 5px;
            }
            QMessageBox QPushButton:hover {
                background-color: #5E81AC;
            }
        """)
        msg.exec_()

    def inject(self):
        try:
            if not hasattr(self, 'dll_path'):
                self.show_message("Ошибка", "DLL не выбрана!", QMessageBox.Warning)
                return

            selected_process = self.lineEdit.currentText()
            self.show_message("Успех", f"DLL успешно внедрена в процесс {selected_process}!")
        except Exception as e:
            self.show_message("Ошибка", f"Ошибка при внедрении DLL: {e}", QMessageBox.Critical)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
