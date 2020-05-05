from PyQt5.QtWidgets import QDialog, QApplication, QVBoxLayout, QLabel
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap

class Window(QDialog):
	def __init__(self):
		super().__init__()

		self.title="PyQt5 Image in Window"
		self.top=50
		self.left=100
		self.width=400
		self.height=300

		self.InitWindow()


	def InitWindow(self):
		self.setWindowIcon(QtGui.QIcon("img\home.png"))
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		
		vbox=QVBoxLayout()

		#Defining Image Label
		labelImage=QLabel(self)
		pixmap=QPixmap("img\\football_players.png")
		labelImage.setPixmap(pixmap)
		vbox.addWidget(labelImage)

		self.setLayout(vbox)

		self.show()


if __name__ == '__main__':
	
	App= QApplication(sys.argv)
	window= Window()
	sys.exit(App.exec())
