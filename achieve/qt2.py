#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''使用 PyQt5 内嵌浏览器浏览网页，并注入 Javascript 脚本实现自动化操作。'''
import os
import random
import re
import sys
import time
from datetime import datetime

import requests
from PyQt5 import QtNetwork
from PyQt5.QtCore import QUrl, pyqtSlot, QThread, pyqtSignal
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEngineScript, QWebEngineSettings
from PyQt5.QtWidgets import (
    QWidget, QApplication, QVBoxLayout, QHBoxLayout,
    QDesktopWidget, QTextEdit, QLabel, QLineEdit, QPushButton,
    QFileDialog, QProgressBar, QComboBox,
)

import req
import settings
from compose.slider_button import SwitchBtn
from dates import dates

requests.packages.urllib3.disable_warnings()

# 构造请求参数
submitParams = {
    'checkinDate': '2022-06-14',
    'houseType': '1',
    't': '1655172000134',
    's': 'bac2e56f23b3a2ce1b5cbd2941b015aa'
}

cookies = ''


# # 创建一个子线程
# class UpdateThread(QThread):
#     # 创建一个信号，触发时传递当前时间给槽函数
#     update_url = pyqtSignal(str)
#
#     def run(self):
#         global cookies
#         res = req.getDetail(cookies)
#         getDetailParams(submitParams, res.text)
#         if len(submitParams) == 2:
#             log('Quota is full')
#             return
#         entry_url = settings.confirmUrl.format(submitParams['checkinDate'], submitParams['t'], submitParams['s'])
#         self.update_url.emit(entry_url)


# 创建一个子线程
class SubmitThread(QThread):
    # 创建一个信号，触发时传递当前时间给槽函数
    submit = pyqtSignal()

    def run(self):
        while True:
            time.sleep(0.05)
            self.submit.emit()


class Browser(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

        # 脚本
        self.profile = QWebEngineProfile.defaultProfile()
        self.profile.setHttpUserAgent(req.user_agents[random.randint(0, 9999)])
        self.script = QWebEngineScript()
        # self.script.setInjectionPoint(QWebEngineScript.DocumentReady)
        self.prepare_script()
        # 绑定cookie被添加的信号槽
        self.profile.cookieStore().cookieAdded.connect(self.__onCookieAdd)
        self.webView.iconChanged.connect(self.__onWindowIconChanged)
        self.webView.titleChanged.connect(self.__onTitleChanged)

    def init_ui(self):
        self.webView = QWebEngineView()

        self.webView.settings().setAttribute(QWebEngineSettings.WebAttribute.ShowScrollBars, False)

        self.logEdit = QTextEdit()
        self.logEdit.setFixedHeight(100)

        self.addrEdit = QLineEdit()
        self.addrEdit.returnPressed.connect(self.load_url)
        self.webView.urlChanged.connect(lambda i: self.urlChange(i.toDisplayString()))
        self.webView.loadFinished.connect(lambda i: self.loadFinish(i))

        self.jsEdit = QLineEdit()
        self.jsEdit.setEnabled(False)
        self.jsEdit.setText(os.path.abspath('inject.js'))

        self.actionChoice = QComboBox()
        self.actionChoice.addItems(['关闭', '开启'])
        self.actionChoice.currentIndexChanged[int].connect(self.actionChange)  # 条目发生改变，发射信号，传递条目内容

        self.slider = SwitchBtn(self)
        self.slider.checkedChanged.connect(self.actionChange)

        self.dateChoice = QComboBox()
        self.dateChoice.addItems(dates)
        self.dateChoice.currentIndexChanged[str].connect(self.dateChange)  # 条目发生改变，发射信号，传递条目内容

        loadUrlBtn = QPushButton('加载')
        loadUrlBtn.clicked.connect(self.load_url)

        chooseJsBtn = QPushButton('选择脚本文件')
        chooseJsBtn.clicked.connect(self.choose_js_file)

        # 导航/工具
        top = QWidget()
        top.setFixedHeight(160)
        topBox = QVBoxLayout(top)
        topBox.setSpacing(0)
        topBox.setContentsMargins(0, 0, 0, 0)

        progBar = QProgressBar()
        progBar.setFixedHeight(10)
        progBar.setTextVisible(False)
        progBox = QHBoxLayout()
        progBox.addWidget(progBar)
        topBox.addLayout(progBox)
        self.webView.loadProgress.connect(progBar.setValue)

        naviBox = QHBoxLayout()
        naviBox.addWidget(QLabel('网址'))
        naviBox.addWidget(self.addrEdit)
        naviBox.addWidget(loadUrlBtn)
        topBox.addLayout(naviBox)

        naviBox = QHBoxLayout()
        naviBox.addWidget(QLabel('脚本'))
        naviBox.addWidget(self.jsEdit)
        naviBox.addWidget(chooseJsBtn)
        topBox.addLayout(naviBox)

        naviBox = QHBoxLayout()
        naviBox.addWidget(QLabel('疯狗'), 1)
        # naviBox.addWidget(self.actionChoice)
        naviBox.addWidget(self.slider, 1)
        naviBox.addWidget(QLabel(), 6)
        naviBox.addWidget(QLabel('日期'), 1)
        naviBox.addWidget(self.dateChoice, 1)
        topBox.addLayout(naviBox)

        # 主界面
        layout = QVBoxLayout(self)
        layout.addWidget(self.webView)
        layout.addWidget(top)
        layout.addWidget(self.logEdit)

        self.show()
        self.resize(665, 844)
        self.center()

    def __onWindowIconChanged(self, icon):
        self.setWindowIcon(icon)

    def __onTitleChanged(self, title):
        self.setWindowTitle(title)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    @pyqtSlot()
    def load_url(self):
        url = self.addrEdit.text().strip()
        # if not url.lower().startswith('http://') \
        #         and not url.lower().startswith('https://'):
        #     url = 'http://{}'.format(url)
        self.load(url)

    @pyqtSlot()
    def choose_js_file(self):
        f, _ = QFileDialog.getOpenFileName(filter="Javascript files(*.js)")
        if os.path.isfile(f):
            self.jsEdit.setText(f)
            self.prepare_script()

    def prepare_script(self):
        path = self.jsEdit.text().strip()
        if not os.path.isfile(path):
            self.log('invalid js path')
            return

        self.profile.scripts().remove(self.script)
        with open(path, 'r') as f:
            jstr = 'const targetIndex = "' + str(self.dateChoice.currentIndex()) + '";' + \
                   'const action = "' + str(int(self.slider.checked)) + '";' + \
                   f.read()
            self.script.setSourceCode(jstr)
        self.profile.scripts().insert(self.script)
        self.log('injected js ready')

    def log(self, msg, *args, **kwargs):
        m = msg.format(*args, **kwargs)
        self.logEdit.append('{} {}'.format(
            datetime.now().strftime('%H:%M:%S'), m))

    def load(self, url):
        self.log(f'loading {url}')
        self.addrEdit.setText(url)
        self.webView.load(QUrl(url))

    @pyqtSlot()
    def urlChange(self, url):
        self.addrEdit.setText(url)
        # if re.search('/userPage/userCenter', url) is not None:
        #     # 创建子线程
        #     self.subThread = UpdateThread()
        #     # 将子线程中的信号与timeUpdate槽函数绑定
        #     self.subThread.update_url.connect(self.load)
        #     # 启动子线程（开始更新时间）
        #     self.subThread.start()
        # if re.search('/passInfo/confirmOrder', url) is not None:
        #     # 创建子线程
        #     self.submitThread = SubmitThread()
        #     # 将子线程中的信号与timeUpdate槽函数绑定
        #     self.submitThread.submit.connect(self.submit)
        #     # 启动子线程（开始更新时间）
        #     self.submitThread.start()
        pass

    @pyqtSlot()
    def loadFinish(self, has):
        if not has:
            return
        url = self.addrEdit.text().strip()
        if re.search('/passInfo/confirmOrder', url) is not None:
            print('start submit listening')
            # 创建子线程
            self.submitThread = SubmitThread()
            # 将子线程中的信号与timeUpdate槽函数绑定
            self.submitThread.submit.connect(self.submit)
            # 启动子线程（开始更新时间）
            self.submitThread.start()
        pass

    def dateChange(self, i):
        self.log(i)
        self.prepare_script()

    def actionChange(self, i):
        if i:
            self.log('格局打开')
        else:
            self.log('格局小了')
        self.prepare_script()

    def submit(self):
        self.webView.page().runJavaScript(
            'document.getElementById("btn_confirmOrder").click()')

    def __onCookieAdd(self, cookie):
        global cookies
        name = cookie.name().data().decode('utf-8')
        value = cookie.value().data().decode('utf-8')
        cookies += (name + '=' + value + ';')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    if settings.proxyEnable is True:
        proxy = QtNetwork.QNetworkProxy()
        proxy.setType(QtNetwork.QNetworkProxy.HttpProxy)
        proxy.setHostName(settings.proxyHost)
        proxy.setPort(settings.proxyPort)
        QtNetwork.QNetworkProxy.setApplicationProxy(proxy)
    b = Browser()
    b.load(settings.userCenterUrl)
    sys.exit(app.exec_())
