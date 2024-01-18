import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, \
    QVBoxLayout, QHBoxLayout, \
    QLabel, QTextEdit, QMessageBox, QDialogButtonBox

from widget_plots import Plots
from widget_commands import Commands
from widget_info import Information

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
        
        
        self.plots = Plots()
        self.commands = Commands()
        self.infomation = Information()
        

        layout = QHBoxLayout()
        layout.addWidget(self.plots)
        
        layout_bc = QVBoxLayout()
        layout_bc.addWidget(self.commands)
        layout_bc.addStretch()
        layout_bc.addWidget(self.infomation)
        layout.addLayout(layout_bc)
        
        self.setLayout(layout)  
    
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())
