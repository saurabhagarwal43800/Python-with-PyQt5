from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QHBoxLayout, QLabel
import sys
from PyQt5 import QtGui, QtCore

class Window(QWidget):

	def __init__(self):

		super().__init__()

		self.title="PyQt5 Whats This"
		self.top=200
		self.left=300
		self.width=400
		self.height=300

		self.InitWindow()


	def InitWindow(self):
		
		self.setWindowIcon(QtGui.QIcon("img\\home.png"))
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)

		hbox=QHBoxLayout()

		label=QLabel("Focus and Press Shift + F1")
		hbox.addWidget(label)

		button=QPushButton("Click Me",self)
		button.setWhatsThis("This is a button you can click")
		hbox.addWidget(button)

		self.setLayout(hbox)

		self.show()


if __name__ == '__main__':
	
	App= QApplication(sys.argv)
	window= Window()
	sys.exit(App.exec())