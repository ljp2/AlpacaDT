import sys
import pandas as pd
import numpy as np
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QHBoxLayout,  \
    QPushButton, QLabel

import pyqtgraph as pg

class Plots(QWidget):
    def __init__(self, df):
        super().__init__()

        self.w = pg.GraphicsLayoutWidget()
        self.w.setBackground('w')

        # Create three subplots
        self.p1 = self.w.addPlot(title="Plot 1")
        self.p2 = self.w.addPlot(title="Plot 2")
        self.p3 = self.w.addPlot(title="Plot 3")

        # Set the subplots in a vertical arrangement
        self.w.nextRow()  # Move to the next row
        self.w.addItem(self.p1)
        self.w.nextRow()  # Move to the next row
        self.w.addItem(self.p2)
        self.w.nextRow()  # Move to the next row
        self.w.addItem(self.p3)

        # Set the x-axis to be shared with plot1
        self.p2.setXLink(self.p1)
        self.p3.setXLink(self.p1)
        # self.p2.setYLink(self.p1)
        # self.p3.setYLink(self.p1)

        xlow = df.index[0]
        xhigh = df.index[-1]
        ylow = df['Low'].min()
        yhigh = df['High'].max()
        for p in [self.p1, self.p2, self.p3]:
            p.setAxisItems({'bottom': pg.DateAxisItem()})
            p.setXRange(xlow, xhigh)
            p.setYRange(ylow, yhigh)

        layout = QVBoxLayout()
        layout.addWidget(self.w)
        self.setLayout(layout)


class Commands(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.button_1 = QPushButton("Button 1")
        self.button_2 = QPushButton("Button 2")
        self.button_3 = QPushButton("Button 3")
        self.button_4 = QPushButton("Button 4")

        self.button_1.clicked.connect(self.on_button_1_clicked)
        self.button_2.clicked.connect(self.on_button_2_clicked)
        self.button_3.clicked.connect(self.on_button_3_clicked)
        self.button_4.clicked.connect(self.on_button_4_clicked)
        
        self.label_1 = QLabel("Label 1")
        self.label_2 = QLabel("Label 2")
        self.label_3 = QLabel("Label 3")
        self.label_4 = QLabel("Label 4")

        layout.addWidget(self.button_1)
        layout.addWidget(self.button_2)
        layout.addWidget(self.button_3)  
        layout.addWidget(self.button_4)
        layout.addStretch()
        layout.addWidget(self.label_1)
        layout.addWidget(self.label_2)  
        layout.addWidget(self.label_3)
        layout.addWidget(self.label_4)
        self.setLayout(layout)


    def on_button_1_clicked(self):
        print("Button 1 clicked")

    def on_button_2_clicked(self):
        print("Button 2 clicked") 

    def on_button_3_clicked(self):
        print("Button 3 clicked")

    def on_button_4_clicked(self):
        print("Button 4 clicked")


        
    


class MainWindow(QMainWindow):
    def __init__(self, df):
        super().__init__()

        self.plots = Plots(df)
        self.commands = Commands()

        layout = QHBoxLayout()
        layout.addWidget(self.plots)
        layout.addWidget(self.commands)

        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)

def main(filename:str):
    df = pd.read_csv(filename, index_col='Datetime', parse_dates=True)
    df.index = df.index = df.index.astype(np.int64) // 10**9
    print(df.head())
    
    app = QApplication(sys.argv)
    main = MainWindow(df)
    main.show()
    sys.exit(app.exec())

    
    
if __name__ == '__main__':
    main('./Data/20240111.csv')
