from PyQt5 import QtWidgets
from ui.mainframe import Ui_MainWindow


class WndProc(QMainWindow):
    def __init__(self):
        super(WndProc, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.path = ''
        self.ui.action_open.connect(self.open_file)
        self.ui.action_save.connect(self.open_file)

    def open_file():
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Открыть", "", "Text Files (*.txt)", options = QtWidgets.QFileDialog.Options())
        if fileName:
            self.path = fileName
            self.ui.plainTextEdit.setText(fileName)

    def save_file():
        if path != '':
            file = open(path, 'w')
            text = self.ui.plainTextEdit.getText()
            file.write(text)
            file.close()

    def save_file_as():
        continue


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = WndProc()
    application.show()
    sys.exit(app.exec())