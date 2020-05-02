from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect

class Window(QMainWindow):
	def __init__(self):
		super().__init__()

		self.title="PyQt5 PushButton"
		self.top=500
		self.left=200
		self.width=300
		self.height=250

		self.InitWindow()


	def InitWindow(self):
		self.setWindowIcon(QtGui.QIcon("home.png"))
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		self.UiComponents()
		self.show()

	# To Create Push Button
	def UiComponents(self):
		button=QPushButton("Click Me", self)
		button.setGeometry(QRect(100,100,111,28))

App= QApplication(sys.argv)
window= Window()
sys.exit(App.exec())
