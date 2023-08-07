# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(680, 430)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 261, 101))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 67, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 67, 17))
        self.label_2.setObjectName("label_2")
        self.ledit_IP = QtWidgets.QLineEdit(self.groupBox)
        self.ledit_IP.setGeometry(QtCore.QRect(50, 27, 113, 25))
        self.ledit_IP.setObjectName("ledit_IP")
        self.ledit_port = QtWidgets.QLineEdit(self.groupBox)
        self.ledit_port.setGeometry(QtCore.QRect(50, 57, 113, 25))
        self.ledit_port.setObjectName("ledit_port")
        self.btn_connect = QtWidgets.QPushButton(self.groupBox)
        self.btn_connect.setGeometry(QtCore.QRect(170, 60, 81, 25))
        self.btn_connect.setObjectName("btn_connect")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(310, 20, 351, 101))
        self.groupBox_2.setObjectName("groupBox_2")
        self.ledit_freq = QtWidgets.QLineEdit(self.groupBox_2)
        self.ledit_freq.setGeometry(QtCore.QRect(100, 30, 113, 25))
        self.ledit_freq.setObjectName("ledit_freq")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 33, 91, 17))
        self.label_3.setObjectName("label_3")
        self.ledit_pwr = QtWidgets.QLineEdit(self.groupBox_2)
        self.ledit_pwr.setGeometry(QtCore.QRect(100, 60, 113, 25))
        self.ledit_pwr.setObjectName("ledit_pwr")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 63, 91, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(220, 35, 67, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(220, 65, 67, 17))
        self.label_6.setObjectName("label_6")
        self.btn_sendfrq = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_sendfrq.setGeometry(QtCore.QRect(260, 30, 81, 25))
        self.btn_sendfrq.setObjectName("btn_sendfrq")
        self.btn_sendpwr = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_sendpwr.setGeometry(QtCore.QRect(260, 60, 81, 25))
        self.btn_sendpwr.setObjectName("btn_sendpwr")
        self.msgbox = QtWidgets.QTextEdit(self.centralwidget)
        self.msgbox.setGeometry(QtCore.QRect(10, 340, 651, 61))
        self.msgbox.setObjectName("msgbox")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 140, 351, 191))
        self.groupBox_3.setObjectName("groupBox_3")
        self.ledit_minf = QtWidgets.QLineEdit(self.groupBox_3)
        self.ledit_minf.setGeometry(QtCore.QRect(100, 30, 113, 25))
        self.ledit_minf.setObjectName("ledit_minf")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(10, 33, 91, 17))
        self.label_7.setObjectName("label_7")
        self.ledit_maxf = QtWidgets.QLineEdit(self.groupBox_3)
        self.ledit_maxf.setGeometry(QtCore.QRect(100, 60, 113, 25))
        self.ledit_maxf.setObjectName("ledit_maxf")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(10, 63, 91, 17))
        self.label_8.setObjectName("label_8")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(10, 93, 91, 17))
        self.label_11.setObjectName("label_11")
        self.ledit_stepS = QtWidgets.QLineEdit(self.groupBox_3)
        self.ledit_stepS.setGeometry(QtCore.QRect(100, 90, 113, 25))
        self.ledit_stepS.setObjectName("ledit_stepS")
        self.ledit_dwellT = QtWidgets.QLineEdit(self.groupBox_3)
        self.ledit_dwellT.setGeometry(QtCore.QRect(100, 120, 113, 25))
        self.ledit_dwellT.setObjectName("ledit_dwellT")
        self.btn_sweep = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_sweep.setGeometry(QtCore.QRect(260, 160, 81, 25))
        self.btn_sweep.setObjectName("btn_sweep")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(10, 123, 91, 17))
        self.label_12.setObjectName("label_12")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(220, 35, 67, 17))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(220, 65, 67, 17))
        self.label_10.setObjectName("label_10")
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(220, 125, 67, 17))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setGeometry(QtCore.QRect(220, 95, 67, 17))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox_3)
        self.label_15.setGeometry(QtCore.QRect(10, 153, 91, 17))
        self.label_15.setObjectName("label_15")
        self.ledit_StartPower = QtWidgets.QLineEdit(self.groupBox_3)
        self.ledit_StartPower.setGeometry(QtCore.QRect(100, 150, 113, 25))
        self.ledit_StartPower.setObjectName("ledit_StartPower")
        self.label_16 = QtWidgets.QLabel(self.groupBox_3)
        self.label_16.setGeometry(QtCore.QRect(220, 155, 67, 17))
        self.label_16.setObjectName("label_16")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RIGOL DSG821"))
        self.groupBox.setTitle(_translate("MainWindow", "RIGOL DSG821 Connection"))
        self.label.setText(_translate("MainWindow", "IP:"))
        self.label_2.setText(_translate("MainWindow", "Port:"))
        self.ledit_IP.setText(_translate("MainWindow", "192.168.0.9"))
        self.ledit_port.setText(_translate("MainWindow", "5555"))
        self.btn_connect.setText(_translate("MainWindow", "Connect"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Fixed Frequency"))
        self.label_3.setText(_translate("MainWindow", "Frequency:"))
        self.label_4.setText(_translate("MainWindow", "Power:"))
        self.label_5.setText(_translate("MainWindow", "MHz"))
        self.label_6.setText(_translate("MainWindow", "dBm"))
        self.btn_sendfrq.setText(_translate("MainWindow", "Send"))
        self.btn_sendpwr.setText(_translate("MainWindow", "Send"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Sweep Parameters"))
        self.label_7.setText(_translate("MainWindow", "Min. Freq:"))
        self.label_8.setText(_translate("MainWindow", "Max Freq:"))
        self.label_11.setText(_translate("MainWindow", "Step Size:"))
        self.btn_sweep.setText(_translate("MainWindow", "Send"))
        self.label_12.setText(_translate("MainWindow", "Dwell Time:"))
        self.label_9.setText(_translate("MainWindow", "MHz"))
        self.label_10.setText(_translate("MainWindow", "MHz"))
        self.label_13.setText(_translate("MainWindow", "Sec."))
        self.label_14.setText(_translate("MainWindow", "MHz"))
        self.label_15.setText(_translate("MainWindow", "Power:"))
        self.label_16.setText(_translate("MainWindow", "dBm"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
