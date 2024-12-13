#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
import threading
import time

from PyQt5.QtWidgets import QApplication, QWidget
from ui.ui_main import Ui_Main
from qttoolset.collector import QTaskCollector, QTaskContext, QTaskNotifier


class HTTPRequestMainWindow(QWidget, Ui_Main):
    def __init__(self, parent=None):
        super(HTTPRequestMainWindow, self).__init__(parent)
        self.task_collector = QTaskCollector(parent=self)
        self.task_collector.start()

    def setup_window(self):
        self.setupUi(self)
        self.setWindowTitle('QtToolset')

    def connect_signals(self):
        self.startBtn.clicked.connect(lambda: self.on_task_startup_handle())
        self.pausedBtn.clicked.connect(lambda: self.task_collector.execute_task("shutdown"))
        self.restartBtn.clicked.connect(lambda: self.task_collector.execute_task("restart"))

    def on_task_startup_handle(self):
        print(" * 启动任务")
        self.task_collector.execute_task("startup")
        self.startBtn.setEnabled(False)

    @QTaskCollector.function("startup")
    def task_startup(self, context: QTaskContext):
        print(threading.current_thread())
        angle_list = [
            [0, 0, 0, 0, 90, 0],
            [10, 20, 30, 40, 90, 40],
            [20, 20, 10, 90, 90, 40],
        ]
        context.send(state='startup', data='data')
        stime = time.time()
        while time.time() - stime < 15:
            for i in range(3):
                context.send(state='running', data='data', index=angle_list[i])
                time.sleep(0.2)
        else:
            context.send(state='finished', data='data')

    @QTaskCollector.callback("startup")
    def task_started(self, notifier: QTaskNotifier):
        print(threading.current_thread().name)
        QApplication.processEvents()
        state = notifier.kwargs.get('state')
        index = notifier.kwargs.get('index')
        if state == 'startup':
            print("Startup", index)
        elif state == 'running':
            print("Running", index)
        elif state == 'finished':
            print("Finished", index)
            self.startBtn.setEnabled(True)

    @QTaskCollector.function("shutdown")
    def task_shutdown(self, notifier: QTaskNotifier):
        print("Shutdown", notifier)

    @QTaskCollector.function("restart")
    def task_restart(self, notifier: QTaskNotifier):
        print("Restart", notifier)

    def initialization(self):
        self.setup_window()
        self.connect_signals()
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = HTTPRequestMainWindow()
    main_window.initialization()
    sys.exit(app.exec_())
