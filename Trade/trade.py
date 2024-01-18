import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout 

from tradePlots import Plots
from tradeCommands import Commands
from tradeInfo import Information

class TradingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Trade")
        
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

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = TradingApp()
    main_window.show()
    sys.exit(app.exec())