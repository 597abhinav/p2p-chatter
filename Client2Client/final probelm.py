#!usr/bin/env python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final probelm.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(637, 480)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 70, 47, 14))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 170, 47, 14))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 280, 47, 14))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 370, 47, 14))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setIconSize(QtCore.QSize(80, 80))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        MainWindow.insertToolBarBreak(self.toolBar)
        self.actionChat = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/f/chat-2-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionChat.setIcon(icon)
        self.actionChat.setObjectName(_fromUtf8("actionChat"))
        self.actionDownload = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/f/Downloads-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDownload.setIcon(icon1)
        self.actionDownload.setObjectName(_fromUtf8("actionDownload"))
        self.actionUpload = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/f/upload-icon-32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUpload.setIcon(icon2)
        self.actionUpload.setObjectName(_fromUtf8("actionUpload"))
        self.actionExit = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/f/exit-button-icon-18.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon3)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.toolBar.addAction(self.actionChat)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionDownload)
        self.toolBar.addAction(self.actionUpload)
        self.toolBar.addAction(self.actionExit)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.toolBar, QtCore.SIGNAL(_fromUtf8("actionTriggered(QAction*)")), self.label.clear)
        QtCore.QObject.connect(self.toolBar, QtCore.SIGNAL(_fromUtf8("actionTriggered(QAction*)")), self.label_2.clear)
        QtCore.QObject.connect(self.toolBar, QtCore.SIGNAL(_fromUtf8("actionTriggered(QAction*)")), self.label_3.clear)
        QtCore.QObject.connect(self.toolBar, QtCore.SIGNAL(_fromUtf8("actionTriggered(QAction*)")), self.label_4.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "TextLabel", None))
        self.label_2.setText(_translate("MainWindow", "TextLabel", None))
        self.label_3.setText(_translate("MainWindow", "TextLabel", None))
        self.label_4.setText(_translate("MainWindow", "TextLabel", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionChat.setText(_translate("MainWindow", "Chat", None))
        self.actionDownload.setText(_translate("MainWindow", "Download", None))
        self.actionUpload.setText(_translate("MainWindow", "Upload", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))

import tttt_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

