import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pandas as pd
import numpy as np

from datetime import datetime, time
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QColor, QPen
import pyqtgraph as pg
import utils

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import alpaca_api

class Plots(QWidget):
    def __init__(self, xlimits=None, ylimits=None):
        super().__init__()
        self.setupPlots(xlimits=xlimits, ylimits=ylimits)
        self.plotFirstData()
        
    def setupPlots(self, xlimits=None, ylimits=None):
        
        xlow, xhigh = utils.todayStartEndUTC()
        bar = alpaca_api.getLatestCryptoBar('BTC/USD', 60*24)
        ylow = bar['Low'][0]
        yhigh = bar['High'][0]
        
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
            # p.setAxisItems({'bottom': pg.DateAxisItem()})
            p.setXRange(xlow, xhigh)
            p.setYRange(ylow, yhigh)

        layout = QVBoxLayout()
        layout.addWidget(self.w)
        self.setLayout(layout)
        
    def plotFirstData(self):
        df = alpaca_api.getRecentBars()
        x = df.index.tz_localize(None).astype(np.int64) // 10**9
        y = df['Close'].values
    
        pen = pg.mkPen(color='k', width=5)
        self.p1.plot(x,y, pen=pen)
        self.p2.plot(x,y, pen=pen)
        self.p3.plot(x,y,pen=pen)
        
