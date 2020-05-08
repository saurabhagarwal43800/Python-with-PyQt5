from PyQt5.QtWidgets import QDialog, QApplication, QVBoxLayout, QHBoxLayout, QLabel, QGroupBox, QCheckBox
import sys
from PyQt5 import QtGui, QtCore

class Window(QDialog):

	def __init__(self):

		super().__init__()

		self.title="PyQt5 CheckBox"
		self.top=200
		self.left=300
		self.width=400
		self.height=300

		self.InitWindow()


	def InitWindow(self):
		
		self.setWindowIcon(QtGui.QIcon("img\\home.png"))
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		
		self.checkBox()		# Calling checkBox function
		vbox=QVBoxLayout()		# Initializing QVboxLayout
		vbox.addWidget(self.groupBox)		# Adding groupBox to vbox

		self.label=QLabel(self)		# Initializing label
		self.label.setFont(QtGui.QFont("Sanserif",15))
		vbox.addWidget(self.label)		# Adding label to vbox
		
		self.setLayout(vbox)

		self.show()

	def checkBox(self):
		
		self.groupBox=QGroupBox("What is your Favorite Programming Language?")	# Initializing QGroupBox with title
		self.groupBox.setFont(QtGui.QFont("Sanserif",13))

		hboxLayout=QHBoxLayout()		# Initializing QHBoxLayout 

		self.check1=QCheckBox("Python")		# Creating CheckBox1
		self.check1.setIcon(QtGui.QIcon("img\\python.png"))
		self.check1.setIconSize(QtCore.QSize(40,40))
		self.check1.setFont(QtGui.QFont("Sanserif",13))
		self.check1.toggled.connect(self.OnCheckBox)	# Calling OnCheckBox function when it is checked and show some text
		hboxLayout.addWidget(self.check1)		# Adding check1 to hboxLayoout

		self.check2=QCheckBox("Java")
		self.check2.setIcon(QtGui.QIcon("img\\java.png"))
		self.check2.setIconSize(QtCore.QSize(40,40))
		self.check2.setFont(QtGui.QFont("Sanserif",13))
		self.check2.toggled.connect(self.OnCheckBox)
		hboxLayout.addWidget(self.check2)

		self.check3=QCheckBox("Ruby")
		self.check3.setIcon(QtGui.QIcon("img\\ruby.png"))
		self.check3.setIconSize(QtCore.QSize(40,40))
		self.check3.setFont(QtGui.QFont("Sanserif",13))
		self.check3.toggled.connect(self.OnCheckBox)
		hboxLayout.addWidget(self.check3)

		self.check4=QCheckBox("C++")
		self.check4.setIcon(QtGui.QIcon("img\\cpp.png"))
		self.check4.setIconSize(QtCore.QSize(40,40))
		self.check4.setFont(QtGui.QFont("Sanserif",13))
		self.check4.toggled.connect(self.OnCheckBox)
		hboxLayout.addWidget(self.check4)

		self.groupBox.setLayout(hboxLayout)		# Adding all the hboxLayout in groupBox

	def OnCheckBox(self):
		checkBox=self.sender()

		if checkBox.isChecked():
			self.label.setText("You have Selected " + checkBox.text())

if __name__ == '__main__':
	
	App= QApplication(sys.argv)
	window= Window()
	sys.exit(App.exec())
