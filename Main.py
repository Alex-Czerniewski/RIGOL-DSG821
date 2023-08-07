#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 20:18:29 2023

@author: Alex
"""

import math
import socket
import sys
import time
import threading
from ui import *
from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets  as qtw
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, 
QLineEdit, QInputDialog)

class Main(qtw.QMainWindow):    
    def __init__(self):        
        super(Main,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)    
        print ("show GUI")
        self.ui.btn_connect.clicked.connect(self.threaded_connec)
        self.ui.btn_sendfrq.clicked.connect(self.threaded_freq)
        self.ui.btn_sendpwr.clicked.connect(self.threaded_pwr)
        self.ui.btn_sweep.clicked.connect(self.threaded_sweep)
        
    # This Function Will Make a Socket Server and, Connect to the Instrument Using The IP and The Port
    def makeConnec(self):
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.settimeout(10)
            print ("Socket successfully created")
        except socket.error as err:
            print ("socket creation failed with error %s" %(err))
        
        host = self.ui.ledit_IP.text()
        port = self.ui.ledit_port.text()
        
        Port = int(port)
        Host = f'{host}'
        
        self.s.connect((Host, Port))
    
    # This Function Will Allow The User To Set The Frequency Of The Signal Unless, The Frequency Is Greater Than 2.1 GHz Or Less Than 9 kHz
    def sigFreq(self):
        freq = self.ui.ledit_freq.text()
        freq=int(float(freq))
        if freq <= 2100 and freq >= 0.009:
            setFreq=":FREQ "+str(freq)+"MHz\r\n"
            self.s.send(setFreq.encode())
            time.sleep(2)
        else:
            print('Please enter a frequency less than 2100 MHz and greater than 0.009 MHz')
    
    # This Function Will Allow The User To Set The Power Of The Signal Unless, The Power Is Greater Than 5 dBm Or Less Than 100 dBm
    def sigPwr(self):
        power = self.ui.ledit_pwr.text()
        power=int(float(power))
        if power <= 5 and power >= -100:
            setPower=":LEV "+str(power)+"dBm"+"\r\n"
            self.s.send(setPower.encode())
            time.sleep(1)
        else:         
            print('Please enter power less than 10dBm and greater than -100 dBm')
    
    # This Function Will Allow The User To Enter The Parameters For The Sweep
    def Sweep(self):                 
        minf = float(self.ui.ledit_minf.text())
        maxf = float(self.ui.ledit_maxf.text())
        stepsize = float(self.ui.ledit_stepS.text())
        SETPOWER = self.ui.ledit_StartPower.text()
        t = self.ui.ledit_dwellT.text()
        
        SETPOWER = int(SETPOWER)
        if SETPOWER <= 5 and SETPOWER >= -100:
            setpower1=":LEV "+str(SETPOWER)+"dBm"+"\r\n"
            self.s.send(setpower1.encode())
        else:
            print('Please enter power less than 10dBm and greater than -100 dBm')
            
        t = int(t)
        
        if minf >= 0.009 and maxf <= 2100:
            f=minf
            while f<=maxf:
             
                cmd = ":FREQ "+str(f)+"MHz\r\n"
                print(cmd)
                self.s.sendall(cmd.encode())
                time.sleep(t)
                f += stepsize
            
            print('Sweep Has Been Completed')
                    
            self.s.sendall(':SOUR:SWE:MODE AUTO\n'.encode())
            self.s.sendall(':OUTP ON\n'.encode())
            self.s.sendall(':SOUR:SWE:EXEC\n'.encode())  
        
        else:
            print('Please enter a frequency less than 2.1 GHz and greater than 0.009 MHz')
        
    # Functions That Start With 'threaded' Is Just To Add Threading To The GUI, This Way It Won't Freeze Will Doing An Action
    def threaded_connec(self):
        t = threading.Thread(target=self.makeConnec)
        t.start()
    
    def threaded_freq(self):
        t = threading.Thread(target=self.sigFreq)
        t.start()
        
    def threaded_pwr(self):
        t = threading.Thread(target=self.sigPwr)
        t.start()
    
    def threaded_sweep(self):
        t = threading.Thread(target=self.Sweep)
        t.start()

if __name__=='__main__':
    
    app=qtw.QApplication([])
    
    widget=Main()
    widget.show()
    
    
    app.exec_()
