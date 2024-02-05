# file : test40_Thread.py
# desc : Qt에서 Thread 동작테스트

import sys
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import QObject
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class BackWorker(QThread): #PyQt에서 스레드 클래스 상속
    initSignal = pyqtSignal(int) # 시그널을 UI스레드로 전달하기 위한 변수객체
    setSignal = pyqtSignal(int)
    setLog = pyqtSignal(str)

    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.parent = parent # BackWorker 에 사용할 멤버 변수

    def run(self) -> None: # Thread 실행
        # Thread 동작할 내용
        maxVal = 1000001
        self.initSignal.emit(maxVal)
        # self.parent.pgbTask.setValue(0) # 프로그레스바 0에서 시작
        # self.parent.pgbTask.setRange(0, maxVal-1) # 0~100
        for i in range(maxVal): # 0 ~ 100
           print_str = f'Thread 출력 > {i}'
           print(print_str)
           self.setSignal.emit(i)
           self.setLog.emit(print_str)
        #    self.parent.txbLog.append(print_str)
        #    self.parent.pgbTask.setValue(i)
    

class qtwin_exam(QWidget):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('./day06/ThreadApp.ui',self) #QtDesinger에서 만든 UI를 load
        # BUTTON에 대한 시그널 처리 
        self.btnStart.clicked.connect(self.btnStartClicked) # UI 파일내에 있는 위젯접근은 VScode상에서 색상으로 표시 x
        
    def btnStartClicked(self):
        th = BackWorker(self)
        th.start() # BackWorker 내의 self.run() 실행
        th.initSignal.connect(self.initPgbTask) # thread 
        th.setSignal.connect(self.setPgbTask)
        th.setLog.connect(self.setTxbLog)  #TextBrowser 위젯에 진행사항 출력


    def closeEvent(self, QCloseEvent) -> None: # X버튼 종료확인
        re = QMessageBox.question(self,'종료 확인','종료 하실?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: # 닫기
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()


    # Thread 에서 시그널이 넘어오면 UI 처리를 대신해주는 부분 슬롯함수
    @pyqtSlot(int)      #BackWorker 스레드에서 self.initSignal.emit() 동작해서 실행
    def initPgbTask(self, maxVal):
        self.pgbTask.setValue(0)
        self.pgbTask.setRange(0, maxVal - 1)
    
    @pyqtSlot(str)      #BackWorker 스레드에서 self.set.emit() 동작해서 실행
    def setTxbLog(self, msg):
        self.txbLog.append(msg)

    @pyqtSlot(int)
    def setPgbTask(self, val):
        self.pgbTask.setValue(val)


if __name__ == '__main__':
    loop = QApplication(sys.argv)
    instance = qtwin_exam()
    instance.show()
    loop.exec_()