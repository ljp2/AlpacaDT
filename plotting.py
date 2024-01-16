import sys
import os

import pandas as pd
import numpy as np
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout

from pyqtgraph import PlotWidget
import pyqtgraph as pg


class PlotLayout(QWidget):
    def __init__(self, df):
        super().__init__()
        self.w = pg.GraphicsLayoutWidget()
        self.w.setBackground('w')
        
        self.p1 = self.w.addPlot(row=0, col=0)
        self.p2 = self.w.addPlot(row=1, col=0)
        self.p3 = self.w.addPlot(row=2, col=0)
        self.p2.setXLink(self.p1)
        self.p3.setXLink(self.p1)
        self.p1.setAxisItems({'bottom': pg.DateAxisItem()})
        self.p2.setAxisItems({'bottom': pg.DateAxisItem()})
        self.p3.setAxisItems({'bottom': pg.DateAxisItem()})

        xlow = df.index[0]
        xhigh = df.index[-1]
        ylow = df['Low'].min()
        yhigh = df['High'].max()
        for p in [self.p1, self.p2, self.p3]:
            p.setXRange(xlow, xhigh)
            p.setYRange(ylow, yhigh)
        
        layout = QVBoxLayout()
        layout.addWidget(self.w)
        self.setLayout(layout)


class MainWindow(QMainWindow):

    def __init__(self, df, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.plotsWidget = PlotLayout(df)
        self.setCentralWidget(self.plotsWidget)
        

def main(filename:str):
    df = pd.read_csv(filename, index_col='Datetime', parse_dates=True)
    df.index = df.index = df.index.astype(np.int64) // 10**9
    print(df.head())
    
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow(df)
    main.show()
    sys.exit(app.exec())

    
    
if __name__ == '__main__':
    main('/Users/ljp2/AlpacaCrypto/Data/20240111.csv')