from PyQt5.QtWidgets import QDialog, QApplication, QVBoxLayout, QLabel
import sys
from PyQt5 import QtGui

class Window(QDialog):
	def __init__(self):
		super().__init__()

		self.title="PyQt5 Label and StyleSheet"
		self.top=500
		self.left=200
		self.width=400
		self.height=300

		self.InitWindow()


	def InitWindow(self):
		self.setWindowIcon(QtGui.QIcon("img\home.png"))
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		
		vbox=QVBoxLayout()

		#Defining First Label
		Label1=QLabel("This is PyQt5 GUI Application Development")
		Label1.setFont(QtGui.QFont("Sanserif",20))
		Label1.setStyleSheet("color:red")
		vbox.addWidget(Label1)

		#Defining Second Label
		Label2=QLabel("This is PyQt5 Label")
		vbox.addWidget(Label2)

		self.setLayout(vbox)

		self.show()


if __name__ == '__main__':
	
	App= QApplication(sys.argv)
	window= Window()
	sys.exit(App.exec())
