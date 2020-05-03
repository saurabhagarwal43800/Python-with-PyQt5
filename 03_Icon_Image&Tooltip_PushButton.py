from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore

class Window(QMainWindow):
	def __init__(self):
		super().__init__()

		self.title="PyQt5 PushButton Icon Image & ToolTip"
		self.top=500
		self.left=200
		self.width=300
		self.height=250

		self.InitWindow()


	def InitWindow(self):
		self.setWindowIcon(QtGui.QIcon("img\\home.png"))
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		self.UiComponents()
		self.show()

	# To Create Push Button
	def UiComponents(self):
		# To create a Push Button
		button=QPushButton("Click Me", self)
		# To give the position, width and height to the button
		button.setGeometry(QRect(100,100,111,50))
		# To set icon on button
		button.setIcon(QtGui.QIcon("home.png"))
		# To set the size of the icon image on button
		button.setIconSize(QtCore.QSize(40,40))
		# To set ToolTip for button i.e. if you hover its shows some tip
		button.setToolTip("<h3>This is click me button</h3>")


App= QApplication(sys.argv)
window= Window()
sys.exit(App.exec())
