import sys
import os
import pandas as pd
import numpy as np

from datetime import datetime, time
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
import pyqtgraph as pg

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import alpaca_api

class Plots(QWidget):
    def __init__(self, xlimits=None, ylimits=None):
        super().__init__()
        self.setupPlots(xlimits=xlimits, ylimits=ylimits)
        self.plotFirstData()
        
    def setupPlots(self, xlimits=None, ylimits=None):
        
        
        if xlimits is None:
            xlow = np.datetime64(datetime.combine(datetime.now().date(), 
                                                  time(0, 0, 0))).astype(np.int64) // 10**6
            xhigh = np.datetime64(datetime.combine(datetime.now().date(), 
                                                   time(23, 59, 0))).astype(np.int64) // 10**6
        else:
            xlow = xlimits[0]
            xhigh = xlimits[1]
        if ylimits is None:
            ylow = 45000
            yhigh = 46000
        else:
            ylow = ylimits[0]
            yhigh = ylimits[1]

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

        for p in [self.p1, self.p2, self.p3]:
            p.setAxisItems({'bottom': pg.DateAxisItem()})
            p.setXRange(xlow, xhigh)
            p.setYRange(ylow, yhigh)

        layout = QVBoxLayout()
        layout.addWidget(self.w)
        self.setLayout(layout)
        
    def plotFirstData(self):
        df = alpaca_api.getRecentBars()
        x = df.index
        y = df['Close'].values
        self.p1.plot(x,y, pen='b')
        self.p2.plot(x,y, pen='b')
        self.p3.plot(x,y, pen='b')
        
        # self.p1.plot(df.index, df['Close'], pen='b')
        # self.p2.plot(df.index, df['High'], pen='g')
        # self.p3.plot(df.index, df['Low'], pen='r')
        
    
