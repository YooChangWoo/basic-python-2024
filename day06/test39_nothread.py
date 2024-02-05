# file : test39_noThread.py
# desc : Qt에서 Thread 없이 동작테스트

import sys
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class qtwin_exam(QWidget):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('./day06/ThreadApp.ui',self) #QtDesinger에서 만든 UI를 load
        # BUTTON에 대한 시그널 처리 
        self.btnStart.clicked.connect(self.btnStartClicked) # UI 파일내에 있는 위젯접근은 VScode상에서 색상으로 표시 x
        

    def btnStartClicked(self):
        maxVal = 1000
        print('시작버튼 클릭')
        self.pgbTask.setValue(0)
        self.pgbTask.setRange(0, maxVal-1) # 0부터 100까지 
        for i in range(maxVal): # 0 ~ 100
           print_str = f'No Thread 출력 > {i}'
           print(print_str)
        self.txbLog.append(print_str)
        self.pgbTask.setValue(i)

        #    print(f'No Thread 출력 > {i}')
        #    self.pgbTask.setValue(i)
        #    self.txbLog.append(f'No Thread 출력 >> {i}')
           
        # self.txbLog.append('상태 : 동작 시작')
    

    def closeEvent(self, QCloseEvent) -> None: # X버튼 종료확인
        re = QMessageBox.question(self,'종료 확인','종료 하실?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: # 닫기
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()
        

    
if __name__ == '__main__':
    loop = QApplication(sys.argv)
    instance = qtwin_exam()
    instance.show()
    loop.exec_()
        
