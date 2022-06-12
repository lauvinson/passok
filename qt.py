import os
import sys

from PyQt5 import QtNetwork, QtCore, QtWebEngineWidgets

import req

os.chdir(os.path.dirname(os.path.abspath(__file__)))
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self, url, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.webview = QtWebEngineWidgets.QWebEngineView()
        # agent = req.user_agents[req.i % 24]
        # self.useragent.defaultProfile().setHttpUserAgent(agent)
        self.resize(390, 844)
        self.webview.load(QtCore.QUrl().fromLocalFile(
            os.path.split(os.path.abspath(__file__))[0] + r'/validate.html'
        ))
        self.webview.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    proxy = QtNetwork.QNetworkProxy()
    proxy.setType(QtNetwork.QNetworkProxy.HttpProxy)
    proxy.setHostName("127.0.0.1")
    proxy.setPort(9999)
    QtNetwork.QNetworkProxy.setApplicationProxy(proxy)
    window = MainWindow()
    # window.show()
    sys.exit(app.exec_())
