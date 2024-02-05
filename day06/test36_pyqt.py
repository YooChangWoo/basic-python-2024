#   file : test36_pyqt.py
# desc: PyQt5 기본화면 만들기

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont
## GUI : Graphic User Interface / CLI : Commmand Line Interface

#print(sys.argv) -> 현재 파이썬파일의 경로표시

class qtwin_exam(QWidget): # QWidget을 상속 받음! QWidget이 가진 모든 것을 사용 가능
    # 생성자
    def __init__(self) -> None:
        super().__init__()
        self.initUI() #화면초기화 함수를 호출
        
    
    def initUI(self):
        self.setGeometry((1920 - 400)//2, (1080 - 300)//2, 400, 200) # x, y, width, height
        self.setWindowTitle('Qt5 Hello World')
        self.text = ' '
        self.show()

    def drawText(self, event, paint):
       paint.setPen(QColor(10,10,10)) # red, green, blue : 0 -> black / red, green, blue : 255 -> white
       paint.setFont(QFont('NanumGothic', 15))
       paint.drawText(300 // 2, 300 // 2, 'HELL WORLD')
       paint.drawText(event.rect(), Qt.AlignCenter, self.text) # AlgrLeft, AlignCenter, AlignRight
     
    def paintEvent(self, event) -> None: # 재정의(Override)
       paint = QPainter()
       paint.begin(self) # paint open
       self.drawText(event, paint)
       paint.end() #paint close
        

loop = QApplication(sys.argv) # 내 소스위치로 앱을 생성할꺼야
instance = qtwin_exam() # Qwidget을 상속한 gtwin_exam 객체를 생성
loop.exec_()
