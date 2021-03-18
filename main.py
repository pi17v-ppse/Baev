from PyQt5 import QtWidgets
from ui.mainframe import Ui_MainWindow


class WndProc(QMainWindow):
    def __init__(self):
        super(WndProc, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def open_file():
        continue

    def open_file_as():
        continue

    def save_file():
        continue

    def save_file_as():
        continue


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = WndProc()
    application.show()
    sys.exit(app.exec())