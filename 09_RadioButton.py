from PyQt5.QtWidgets import QDialog, QApplication, QVBoxLayout, QHBoxLayout, QLabel, QGroupBox, QRadioButton
import sys
from PyQt5 import QtGui, QtCore

class Window(QDialog):

	def __init__(self):

		super().__init__()

		self.title="PyQt5 Radio Button"
		self.top=200
		self.left=300
		self.width=400
		self.height=300

		self.InitWindow()


	def InitWindow(self):
		
		self.setWindowIcon(QtGui.QIcon("img\\home.png"))
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		
		self.radioButton()		# Calling radioButton function
		vbox=QVBoxLayout()		# Initializing QVboxLayout
		vbox.addWidget(self.groupBox)		# Adding groupBox to vbox

		self.label=QLabel(self)		# Initializing label
		self.label.setFont(QtGui.QFont("Sanserif",15))
		vbox.addWidget(self.label)		# Adding label to vbox
		
		self.setLayout(vbox)

		self.show()

	def radioButton(self):
		
		self.groupBox=QGroupBox("What is your Favorite Sports?")	# Initializing QGroupBox with title
		self.groupBox.setFont(QtGui.QFont("Sanserif",13))

		hboxLayout=QHBoxLayout()		# Initializing QHBoxLayout 

		self.radiobtn1=QRadioButton("Football")		# Creating RadioButton1
		self.radiobtn1.setChecked(True)		# Making this radioButton default Checked
		self.radiobtn1.setIcon(QtGui.QIcon("img\\football.png"))
		self.radiobtn1.setIconSize(QtCore.QSize(40,40))
		self.radiobtn1.setFont(QtGui.QFont("Sanserif",13))
		self.radiobtn1.toggled.connect(self.OnRadioBtn)		# Calling OnRadioBtn function when it is checked and show some text
		hboxLayout.addWidget(self.radiobtn1)		# Adding radioButton1 to hboxLayoout

		self.radiobtn2=QRadioButton("Cricket")
		self.radiobtn2.setIcon(QtGui.QIcon("img\\cricket.png"))
		self.radiobtn2.setIconSize(QtCore.QSize(40,40))
		self.radiobtn2.setFont(QtGui.QFont("Sanserif",13))
		self.radiobtn2.toggled.connect(self.OnRadioBtn)
		hboxLayout.addWidget(self.radiobtn2)

		self.radiobtn3=QRadioButton("Tennis")
		self.radiobtn3.setIcon(QtGui.QIcon("img\\tennis.png"))
		self.radiobtn3.setIconSize(QtCore.QSize(40,40))
		self.radiobtn3.setFont(QtGui.QFont("Sanserif",13))
		self.radiobtn3.toggled.connect(self.OnRadioBtn)
		hboxLayout.addWidget(self.radiobtn3)

		self.groupBox.setLayout(hboxLayout)		# Adding all the hboxLayout in groupBox

	def OnRadioBtn(self):
		radioBtn=self.sender()

		if radioBtn.isChecked():
			self.label.setText("You have Selected " + radioBtn.text())


if __name__ == '__main__':
	
	App= QApplication(sys.argv)
	window= Window()
	sys.exit(App.exec())
