# This adds a chart that updates periodically 
# requires pyqtgraph and PyQt5  <- use pip to install if unavailable, we are using python 3.6.3
import threading 
import pyqtgraph as pg
from PyQt5 import QtCore, QtGui

def display_graph():
    win = pg.GraphicsWindow()
    win.setWindowTitle('Live Crypto Price')
    plot1 = win.addPlot()
    curve1 = plot1.plot(pen = 'y')
    
    QtGui.QApplication.instance().exec_()

if __name__ == '__main__':
    display_graph()
    graph_thread = threading.Thread(target=display_graph, args=('display_thread',))
    
    
