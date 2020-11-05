from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(532, 938)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        MainWindow.setInputMethodHints(Qt.ImhTime)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.linedt_TypeMessage = QLineEdit(self.frame)
        self.linedt_TypeMessage.setObjectName(u"linedt_TypeMessage")
        font = QFont()
        font.setFamily(u"OCR-A BT")
        font.setPointSize(16)
        self.linedt_TypeMessage.setFont(font)
        self.linedt_TypeMessage.setAcceptDrops(True)
        self.linedt_TypeMessage.setStyleSheet(u"alternate-background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(255, 255, 255, 255), stop:0.373979 rgba(255, 255, 255, 255), stop:0.373991 rgba(33, 30, 255, 255), stop:0.624018 rgba(33, 30, 255, 255), stop:0.624043 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"color: rgb(0, 245, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"")

        self.gridLayout_2.addWidget(self.linedt_TypeMessage, 2, 1, 1, 1)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"color: rgb(0, 255, 0);")
        self.pushButton.setIconSize(QSize(30, 40))

        self.gridLayout_2.addWidget(self.pushButton, 2, 2, 1, 1)

        self.listContent = QListView(self.frame)
        self.listContent.setObjectName(u"listContent")
        font1 = QFont()
        font1.setPointSize(12)
        self.listContent.setFont(font1)
        self.listContent.setStyleSheet(u"background-color: rgb(0, 255, 255);\n"
"background-color: rgb(170, 255, 255);")
        self.listContent.setInputMethodHints(Qt.ImhNone)

        self.gridLayout_2.addWidget(self.listContent, 1, 0, 1, 3)


        self.gridLayout.addWidget(self.frame, 2, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setSizeIncrement(QSize(0, 30))
        self.label.setBaseSize(QSize(0, 30))
        font2 = QFont()
        font2.setFamily(u"8514oem")
        font2.setPointSize(30)
        font2.setBold(True)
        font2.setWeight(75)
        self.label.setFont(font2)
        self.label.setLayoutDirection(Qt.RightToLeft)
        self.label.setStyleSheet(u"color: rgb(255, 255, 0);\n"
"color: rgb(0, 255, 0);")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 532, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"My chatbot", None))
#if QT_CONFIG(whatsthis)
        self.linedt_TypeMessage.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Yu Gothic UI'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.linedt_TypeMessage.setText("")
        self.linedt_TypeMessage.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type a message....", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Sent", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Robot", None))
    # retranslateUi

