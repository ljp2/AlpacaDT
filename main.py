import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, \
    QLabel, QTextEdit, QMessageBox, QDialogButtonBox
from PyQt6.QtGui import QPixmap

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt6 Application'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        # Create widget for displaying graphics
        self.graphic = QPixmap("image.png")
        self.graphicLabel = QLabel()
        self.graphicLabel.setPixmap(self.graphic)
        
        # Create buttons
        self.button1 = QPushButton('Button 1')
        self.button2 = QPushButton('Button 2')  
        
        self.button_box = QDialogButtonBox()
        self.button_box.addButton(self.button1, QDialogButtonBox.ButtonRole.ActionRole)
        self.button_box.addButton(self.button2, QDialogButtonBox.ButtonRole.ActionRole)
        
        # Create display
        self.display = QTextEdit()
        
        # Set layout
        grid = QGridLayout()
        grid.addWidget(self.graphicLabel, 0, 0) 
        grid.addWidget(self.button_box, 0, 1)
        grid.addWidget(self.display, 2, 0, 1, 2)
        
        self.setLayout(grid)
        
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())
