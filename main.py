from PyQt5 import QtWidgets
from ui.mainframe import Ui_MainWindow


class WndProc(QMainWindow):
    def __init__(self):
        super(WndProc, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.action_open.connect(self.open_file)
        self.ui.action_save_as.connect(self.save_as_file)

    def open_file():
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Открыть", "", "Text Files (*.txt)", options = QtWidgets.QFileDialog.Options())
        if fileName:
            self.ui.plainTextEdit.setText(fileName)

    def save_file():
        continue

    def save_file_as():
        options = QtWidgets.QFileDialog.Options()
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Сохранить как...", "", "Text Files (*.txt)", options)
        if fileName:
            file = open(fileName, 'w')
            text = self.ui.plainTextEdit.getText()
            file.write(text)
            file.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = WndProc()
    application.show()
    sys.exit(app.exec())