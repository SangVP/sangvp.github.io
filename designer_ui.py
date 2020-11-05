from PySide2 import QtWidgets
from UI import Qtlayout


class MyQtApp(Qtlayout.Ui_MainWindow , QtWidgets.QMainWindow):
        def __init__(self):
            super(MyQtApp, self).__init__()
            self.setupUi(self)

        def fill_message(self):
            type_message = self.linedt_TypeMessage.text()
            print(type_message)

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()


