from PyQt5 import QtWidgets
from ui.frame import Ui_MainWindow


""" Обработчик событий пользовательского интерфейса

    Содержит обработчики событий,
    функции, вызываемые в рамках работы с
    пользовательским интерфейсом

    @author     UNKNOWN
    @version    1.1
    @copyright  GNU Public License
    @todo       Реализовать функции открытия и сохранения
"""
class WndProc(QMainWindow):
    def __init__(self):
        super(WndProc, self).__init__()
        """ Контейнер с параметрами пользовательского интерфейса

            @var            ui
        """
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        """ Путь к открытому файлу

            Используется для применения изменений непосредственно
            к открытому файлу

            @var    string  path
        """
        self.path = ''
        
        self.ui.action_open.connect(self.open_file)
        self.ui.action_save.connect(self.save_file)
        self.ui.action_save_as.connect(self.save_as_file)

    """ Функция открытия файла {}

        Открывает выбранный файл
        и передает содержимое файла
        в текстовое поле приложения;
        в случае, если файл не был выбран
        не происходит ничего

        @param      null
        @return     null
    """
    def open_file():
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Открыть", "", "Text Files (*.txt)", options = QtWidgets.QFileDialog.Options())
        if fileName:
            self.path = fileName
            self.ui.plainTextEdit.setText(fileName)

    """ Функция сохранения файла {}

        Сохраняет изменения, внесенные
        во время редактирования файла через
        приложение; если файл не был открыт,
        а работа велась без фиксации изменений
        на носителе, тогда вызывается функция
        Функция сохранения файла как {}

        @param      null
        @return     null
    """
    def save_file():
        if path != '':
            file = open(path, 'w').write(self.ui.plainTextEdit.getText())
        else:
            self.save_file_as()

    """ Функция сохранения файла как {}

        Данные в текстовом поле приложения
        сохраняет на носителе в выбранном пользователем
        месте; в случае, если пользователь нажал "Отмена",
        данные не сохранятся

        @param      null
        @return     null
    """
    def save_file_as():
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Сохранить как...", "", "Text Files (*.txt)", options = QtWidgets.QFileDialog.Options())
        if fileName:
            open(fileName, 'w').write(self.ui.plainTextEdit.getText())


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = WndProc()
    application.show()
    sys.exit(app.exec())