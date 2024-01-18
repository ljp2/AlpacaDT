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
        
        
        
    
if __name__ == '__main__':
    filename = './Data/20240111.csv'
    df = pd.read_csv(filename, index_col='Datetime', parse_dates=True)
    df.index = df.index = df.index.astype(np.int64) // 10**9
    
    app = QApplication(sys.argv)
    main = Plots(df)
    main.show()
    sys.exit(app.exec())