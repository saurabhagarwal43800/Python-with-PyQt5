from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QLabel, QLineEdit
import sys
from PyQt5 import QtGui, QtCore

class Window(QWidget):

	def __init__(self):

		super().__init__()

		self.title="PyQt5 Line Edit"
		self.top=200
		self.left=300
		self.width=400
		self.height=300

		self.InitWindow()


	def InitWindow(self):
		
		self.setWindowIcon(QtGui.QIcon("img\\home.png"))
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)

		hbox=QHBoxLayout()		# Initializing HBoxLayout

		self.lineedit=QLineEdit(self)		# Initializing LineEdit
		self.lineedit.setFont(QtGui.QFont("Sanserif",15))
		self.lineedit.returnPressed.connect(self.OnPressed)
		hbox.addWidget(self.lineedit)

		self.label=QLabel(self)		# Initializing Label
		self.label.setFont(QtGui.QFont("Sanserif",15))
		hbox.addWidget(self.label)

		self.setLayout(hbox)

		self.show()

	def OnPressed(self):

		self.label.setText(self.lineedit.text())


if __name__ == '__main__':
	
	App= QApplication(sys.argv)
	window= Window()
	sys.exit(App.exec())