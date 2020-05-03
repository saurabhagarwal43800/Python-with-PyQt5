from PyQt5.QtWidgets import QDialog, QPushButton, QApplication, QGroupBox, QHBoxLayout, QVBoxLayout
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore

class Window(QDialog):
	def __init__(self):
		super().__init__()

		self.title="PyQt5 Layout Management"
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
		self.groupBox= QGroupBox("What is your favorite Sport?")
		hboxlayout=QHBoxLayout()
		
		# To create a Football Button
		button1=QPushButton("Football", self)
		button1.setIcon(QtGui.QIcon("img\\football.png"))
		button1.setIconSize(QtCore.QSize(40,40))
		button1.setMinimumHeight(40)
		hboxlayout.addWidget(button1)

		# To create a Cricket Button
		button2=QPushButton("Cricket", self)
		button2.setIcon(QtGui.QIcon("img\\cricket.png"))
		button2.setIconSize(QtCore.QSize(40,40))
		button2.setMinimumHeight(40)
		hboxlayout.addWidget(button2)

		# To create a Tennis Button
		button3=QPushButton("Tennis", self)
		button3.setIcon(QtGui.QIcon("img\\tennis.png"))
		button3.setIconSize(QtCore.QSize(40,40))
		button3.setMinimumHeight(40)
		hboxlayout.addWidget(button3)

		self.groupBox.setLayout(hboxlayout)



App= QApplication(sys.argv)
window= Window()
sys.exit(App.exec())
