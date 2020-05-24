import sys
import PySide2
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *




# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):
    def mainScreen(self):
        print('bruh')
        self.stackPane.setCurrentIndex(0)

    def newFileScreen(self):
        print('hello')
        self.stackPane.setCurrentIndex(1)

    def insertElement(self):
        maxElements = 10
        print('meme')
        elementList = []
        num = self.mainPreviewVBox.count()
        if num > 0:
            self.mainPreviewVBox.itemAt(num - 1).changeSize(0,0)

        self.mainPreviewVBox.addSpacing(50)
        self.mainPreviewVBox.addWidget(QLabel('hello'))
        self.mainPreviewVBox.addSpacing((maxElements - len(elementList) + 1) * 75)

    def save(self):
        print("saveee")

    def export():
        print("exporttt")



    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        """
        HOME PAGE UI CODE
        """
        self.setWindowTitle("APP NAME")
        self.setStyleSheet('background-color: rgb(255, 230, 232)')
        self.homeHBox = QHBoxLayout(self)
        self.homeVBox = QVBoxLayout(self)
        self.homeV2Box = QVBoxLayout(self)
        self.homeH2Box = QHBoxLayout(self)

        self.homeAppName = QLabel("App Name")
        self.homeAppName.setFont(QFont("Times", 36, QFont.Bold))
        self.homeAppName.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.homeVBox.addWidget(self.homeAppName)

        self.homeHomeButton = QPushButton("Home")
        self.homeHomeButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.homeH2Box.addWidget(self.homeHomeButton)
        self.homeHomeButton.setFont(QFont("Times", 36, QFont.Bold))
        self.homeHomeButton.setStyleSheet("""
        QWidget {
            border: 0.5px solid gray;
            background-color: rgb(173, 216, 230);
            }
        """)

        self.homeNewFileButton = QPushButton("New File")
        self.homeNewFileButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.homeNewFileButton.setFont(QFont("Times", 36, QFont.Bold))

        self.homeNewFileButton.clicked.connect(self.newFileScreen)
        self.homeNewFileButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.homeNewFileButton.clicked.connect(self.newFileScreen)
        self.homeH2Box.addWidget(self.homeNewFileButton)
        self.homeNewFileButton.setStyleSheet("""
        QWidget {
            border: 0.5px solid gray;
            background-color: rgb(173, 216, 230);
            }
        """)

        self.homeOpenFileButton = QPushButton("Open File")
        self.homeOpenFileButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.homeOpenFileButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.homeOpenFileButton.setFont(QFont("Times", 36, QFont.Bold))
        self.homeH2Box.addWidget(self.homeOpenFileButton)
        self.homeOpenFileButton.setStyleSheet("""
        QWidget {
            border: 0.5px solid gray;
            background-color: rgb(173, 216, 230);
            }
        """)

        self.homeAppText = QLabel("One dollar and eighty-seven cents. That was all. And sixty cents of it was in pennies. Pennies saved one and two at a time by bulldozing the grocer and the vegetable man and the butcher until one’s cheeks burned with the silent imputation of parsimony that such close dealing implied. One dollar and eighty-seven cents. And the next day would be Christmas...jjjjjj jjjjjjjjjj jjjjjjjjjjj jjjjjjj jjjjjjjjjj jjjjj jjjjjj jjjj jjjjj jjjjjjj jjjjj jjjjj jjj jjjL OLO LOL")
        self.homeAppText.setWordWrap(True)
        self.homeAppText.setFont(QFont("Times", 24, QFont.Bold))

        self.homeFormatingVBox = QVBoxLayout(self)
        self.homeFormatingVBox.addWidget(self.homeAppText)
        self.homeFormatingVBox.addSpacing(500)

        self.homeVBox.addLayout(self.homeHBox)
        self.homeV2Box.addWidget(self.homeAppName)
        self.homeHBox.addSpacing(1)
        self.homeV2Box.addLayout(self.homeFormatingVBox)
        self.homeHBox.addLayout(self.homeV2Box)
        self.homeVBox.addLayout(self.homeH2Box)
        self.homeBox = QHBoxLayout(self)


        self.homeWidget = QWidget()
        self.homeWidget.setLayout(self.homeVBox)
        """
        END OF HOME PAGE UI
        """

        """
        START OF MAIN PAGE UI
        """
        self.mainVBox = QVBoxLayout(self)
        self.mainTabHBox = QHBoxLayout(self)

        self.mainHomeAction = QAction('&Home')
        self.mainHomeAction.triggered.connect(self.mainScreen)

        self.mainExportAction = QAction('&Export')
        self.mainExportAction.triggered.connect(self.export)

        self.mainSaveAction = QAction('&Save')
        self.mainSaveAction.triggered.connect(self.save)

        # self.mainFileMenuBar = QMenuBar()
        # self.mainFileMenu = self.mainFileMenuBar.addMenu('&File')
        # self.mainFileMenu.addAction(self.mainHomeAction)


        self.mainFileButton = QPushButton("File")
        self.mainFileButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.mainFileButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.mainFileButton.setMenu(QMenu(self.mainFileButton))
        self.mainFileButton.menu().addAction(self.mainHomeAction)
        self.mainFileButton.menu().addAction(self.mainSaveAction)
        self.mainFileButton.menu().addAction(self.mainExportAction)

        self.mainInsertButton = QPushButton("Insert")
        self.mainInsertButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.mainInsertButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.mainInsertButton.clicked.connect(self.insertElement)

        self.mainTabHBox.addWidget(self.mainFileButton)
        self.mainTabHBox.addWidget(self.mainInsertButton)
        self.mainTabHBox.addSpacing(1650)

        self.mainTabWidget = QWidget()
        self.mainTabWidget.setLayout(self.mainTabHBox)

        self.mainPreviewVBox = QVBoxLayout(self)
        self.mainPreviewWidget = QWidget()
        self.mainPreviewWidget.setLayout(self.mainPreviewVBox)
        self.mainPreviewWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.mainPreviewWidget.setStyleSheet("""
        QWidget {
            border: 0.5px solid gray;
            background-color: rgb(245, 245, 220);
            }
        """)
        self.mainScroll = QScrollArea()
        self.mainScroll.setWidget(self.mainPreviewWidget)
        self.mainScroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.mainScroll.setWidgetResizable(True)

        self.mainPageSimHBox = QHBoxLayout(self)
        self.mainPageSimHBox.addSpacing(600)
        self.mainPageSimHBox.addWidget(self.mainScroll)
        self.mainPageSimHBox.addSpacing(600)

        self.mainVBox.addWidget(self.mainTabWidget)
        # self.mainVBox.addSpacing(10)
        self.mainVBox.addLayout(self.mainPageSimHBox)

        # self.mainVBox.addSpacing()

        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.mainVBox)



        """
        END OF MAIN PAGE UI
        """
        self.stackPane = QStackedLayout(self)
        self.stackPane.addWidget(self.homeWidget)
        self.stackPane.addWidget(self.mainWidget)

        self.widget = QWidget()
        self.widget.setLayout(self.stackPane)


        # self.setLayout(self.hBox)
        # self.homePage = HomePageWidget(self)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(self.widget)

# class HomePageWidget(QWidget):
#     def onPushNewFile(parent):
#         print('hello')
#         parent.hide()
#
#
#
#
#     def __init__(self, parent):
#         super(HomePageWidget, self).__init__(parent)
#         self.hBox = QHBoxLayout(self)
#         self.vBox = QVBoxLayout(self)
#
#         self.label = QLabel("App Name")
#         self.label.setFont(QFont("Times", 36, QFont.Bold))
#         self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
#         self.vBox.addWidget(self.label)
#
#         self.button1 = QPushButton("Home")
#         self.button1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#         self.vBox.addWidget(self.button1)
#
#         self.button2 = QPushButton("New File")
#         self.button2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#         self.button2.clicked.connect(self.onPushNewFile)
#         self.vBox.addWidget(self.button2)
#
#         self.button3 = QPushButton("Open File")
#         self.button3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#         self.vBox.addWidget(self.button3)
#
#         self.hBox.addLayout(self.vBox)
#         self.hBox.addStretch()
#         self.hBox.addStretch()
#         self.hBox.addStretch()
#         self.hBox.addStretch()
#         self.hBox.addStretch()
#         self.hBox.addStretch()
#         self.hBox.addStretch()
#         self.hBox.addStretch()
#
#
#         self.setLayout(self.hBox)


app = QApplication(sys.argv)

window = MainWindow()
window.showMaximized()

app.exec_()
