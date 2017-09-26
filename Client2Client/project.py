#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import socket
import select

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
def download():
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	host = raw_input("Enter Hostname ")
	port = input("Enter port")
	s.connect((host, port))


	while True:
		filename = raw_input("Filename? -> ")
		print filename
		if filename != 'q':
			s.send(filename)
			data = s.recv(1024)
        		if data[:6] == 'EXISTS':
			       	filesize = long(data[6:])
        			message = raw_input("File exists, " + str(filesize) +"Bytes, download? [Y/N]? -> ")
				if message == 'Y' or message == 'y':
        				s.send("OK")
        		       		f = open('new_'+filename, 'wb')
		 		        data = s.recv(1024)
        	    	        	totalRecv = len(data)
	        	       		f.write(data)
			            	while totalRecv < filesize:
        			       		data = s.recv(1024)
       		       				totalRecv += len(data)
		             			f.write(data)
       		        			print "{0:.2f}".format((totalRecv/float(filesize))*100)+ "% Done"
	               			print "Download Complete!"
	                		f.close()
				else:
					break

			else:
				print "File Does Not Exist!"

		else:
			break
	s.close()
def chat():
	# Information of our server to connect to
	HOST = raw_input("Enter host name")
	PORT = input("Enter PORT")

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((HOST, PORT))

	# Client loop
	username = raw_input("Please Enter your username ")
	while True:
        	# Let the user enter some data to send
	        data = raw_input("Message>>")
 		read, write, error = select.select([],[sock],[],0)
    		if len(write)!=0:
	    	# Send the data to the server
        		msg = username+">> "+data
        		b = sock.send(msg)

	    # The receiving loop
    			while True:
           		# When receiving, use the timeout of 1 to receive more data
        			read, write, error = select.select([sock],[],[],1)

        # If there is data, print it
        			if len(read)!=0:
 			        	data = bytes.decode(sock.recv(1024))
			                print data
           
        # Exit the loop if no more data
        	else:
            		break
           


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(640, 480)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 150, 85, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 220, 85, 27))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 300, 85, 27))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 160, 47, 14))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 230, 47, 14))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(350, 310, 47, 14))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), chat)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), download)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.label_3.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton_2.setText(_translate("MainWindow", "Chat", None))
        self.pushButton_3.setText(_translate("MainWindow", "Download", None))
        self.pushButton_4.setText(_translate("MainWindow", "Upload", None))
        self.label.setText(_translate("MainWindow", "TextLabel", None))
        self.label_2.setText(_translate("MainWindow", "TextLabel", None))
        self.label_3.setText(_translate("MainWindow", "TextLabel", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

