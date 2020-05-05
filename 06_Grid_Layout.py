from PyQt5.QtWidgets import QDialog, QPushButton, QApplication, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore

class Window(QDialog):
	def __init__(self):
		super().__init__()

		self.title="PyQt5 Grid Layout Management"
		self.top=500
		self.left=200
		self.width=300
		self.height=250

		self.InitWindow()


	def InitWindow(self):
		self.setWindowIcon(QtGui.QIcon("img\\home.png"))
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		
		self.createLayout()
		vbox=QVBoxLayout()
		vbox.addWidget(self.groupBox)
		self.setLayout(vbox)

		self.show()

	def createLayout(self):
		
		self.groupBox= QGroupBox("What is your favorite Programming Language?")
		#Initializing gridLayout variable as QGridLayout()
		gridLayout=QGridLayout()
		
		# To create a Python Button
		button1=QPushButton("Python", self)
		button1.setIcon(QtGui.QIcon("img\\python.png"))
		button1.setIconSize(QtCore.QSize(40,40))
		button1.setMinimumHeight(40)
		gridLayout.addWidget(button1,0,0)

		# To create a Java Button
		button2=QPushButton("Java", self)
		button2.setIcon(QtGui.QIcon("img\\java.png"))
		button2.setIconSize(QtCore.QSize(40,40))
		button2.setMinimumHeight(40)
		gridLayout.addWidget(button2,0,1)

		# To create a Ruby Button
		button3=QPushButton("Ruby", self)
		button3.setIcon(QtGui.QIcon("img\\ruby.png"))
		button3.setIconSize(QtCore.QSize(40,40))
		button3.setMinimumHeight(40)
		gridLayout.addWidget(button3,1,0)

		# To create a C++ Button
		button4=QPushButton("C++", self)
		button4.setIcon(QtGui.QIcon("img\\cpp.png"))
		button4.setIconSize(QtCore.QSize(40,40))
		button4.setMinimumHeight(40)
		gridLayout.addWidget(button4,1,1)

		self.groupBox.setLayout(gridLayout)


if __name__ == '__main__':
	
	App= QApplication(sys.argv)
	window= Window()
	sys.exit(App.exec())
