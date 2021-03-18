from PyQt5 import QtWidgets
from ui.mainframe import Ui_MainWindow


class WndProc(QMainWindow):
    def __init__(self):
        super(WndProc, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.action_open.connect(self.open_file)

    def open_file():
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Открыть", "", "Text Files (*.txt)", options = QtWidgets.QFileDialog.Options())
        if fileName:
            self.ui.plainTextEdit.setText(fileName)

    def save_file():
        continue

    def save_file_as():
        continue


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = WndProc()
    application.show()
    sys.exit(app.exec())