#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import threading
import time
import traceback
from typing import Callable, Dict, Union
from PyQt5.QtCore import pyqtSignal, QThreadPool, QThread, QRunnable
import queue


class Dispatcher:
    def dispatch(self, collector: 'QTaskCollector', taskid: str, context: 'QTaskContext'):
        raise NotImplementedError


class MappingDispatcher(Dispatcher):
    def dispatch(self, collector, taskid: str, context):
        try:
            metatask = collector.metatask_table.get(taskid, None)
            if metatask is not None:
                metatask.callback(collector.parent(), context)
        except Exception as e:
            traceback.print_exc()
            print(e)


class QTaskNotifier:
    def __init__(self, context: 'QTaskContext', *args, **kwargs):
        self.context = context
        self.taskid = context.taskid
        self.args = args
        self.kwargs = kwargs


class QTaskContext(QRunnable):
    def __init__(self, notifier, metatask: 'QMetatask', parent=None, *args, **kwargs):
        super().__init__()
        self.__notifier = notifier
        self.__metatask = metatask
        self.parent = parent
        self.args = args
        self.kwargs = kwargs
        self.taskid = metatask.taskid
        self.__next_tick_event = threading.Event()
        self.__next_tick_running = False

    def next_tick(self, run: bool = True):
        self.__next_tick_running = run
        self.__next_tick_event.set()

    def wait_next_tick(self):
        while self.__next_tick_event.wait() is False:
            time.sleep(1)
        self.__next_tick_event.clear()
        return self.__next_tick_running

    def send(self, **kwargs):
        try:
            notifier = QTaskNotifier(context=self, **kwargs)
            self.__notifier.emit(self.__metatask.taskid, notifier)
        except Exception as e:
            print(e)

    def run(self):
        self.__metatask.execute(self.parent, self, *self.args, **self.kwargs)


class QMetatask:
    def __init__(self, taskid: str, function: Callable = None, callback: Callable = None):
        self.taskid = taskid
        self.__function = function
        self.__callback = callback

    def set_callback(self, callback: Callable):
        self.__callback = callback

    def set_function(self, function: Callable):
        self.__function = function

    def execute(self, parent, context: QTaskContext, *args, **kwargs):
        self.__function(parent, context, *args, **kwargs)

    def callback(self, parent, context: QTaskContext):
        if self.__callback is not None:
            self.__callback(parent, context)


class QTaskCollector(QThread):
    metatask_table: Dict[str, QMetatask] = {}
    noticed = pyqtSignal(str, object)

    def __init__(self, callback_dispatcher: Callable = None, parent=None):
        super().__init__(parent)
        self.task_queue = queue.Queue()
        self.pool = QThreadPool(parent=parent)
        self.pool.setMaxThreadCount(5)
        self.noticed.connect(self.__notification_collector)
        self.callback_dispatcher = callback_dispatcher
        self.dispatcher = MappingDispatcher()

    def register_callback_dispatcher(self, dispatcher: Union[Callable[['QTaskCollector', str, QTaskContext], None], Dispatcher]):
        # 注册回调派发器
        self.callback_dispatcher = dispatcher

    def __notification_collector(self, taskid, context):
        if self.callback_dispatcher is None:
            self.dispatcher.dispatch(self, taskid, context)

        elif isinstance(self.callback_dispatcher, Dispatcher):
            self.callback_dispatcher.dispatch(self, taskid, context)

    @classmethod
    def add_function_or_callback(cls, taskid: str, callfunc: Callable, is_callback: bool = False):
        metatask_task = cls.metatask_table.get(taskid, None)
        if metatask_task is None:
            metatask_task = QMetatask(taskid=taskid, function=callfunc)
            cls.metatask_table[taskid] = metatask_task

        if is_callback:
            metatask_task.set_callback(callfunc)
        else:
            metatask_task.set_function(callfunc)

    @classmethod
    def function(cls, taskid: str):
        def decorator(func):
            cls.add_function_or_callback(taskid=taskid, callfunc=func, is_callback=False)
        return decorator

    @classmethod
    def callback(cls, taskid: str):
        def decorator(func):
            cls.add_function_or_callback(taskid=taskid, callfunc=func, is_callback=True)
        return decorator

    def execute_task(self, taskid: str, *args, **kwargs):
        self.task_queue.put((taskid, args, kwargs))

    def clear_tasks(self):
        self.task_queue.empty()
        self.pool.clear()
        self.pool.waitForDone()

    def _task_context_builder(self, metatask: QMetatask, *args, **kwargs):
        return QTaskContext(
            notifier=self.noticed,
            metatask=metatask,
            parent=self.parent(),
            *args,
            **kwargs
        )

    def run(self):
        while True:
            try:
                taskid, args, kwargs = self.task_queue.get(timeout=3)
                metatask = self.metatask_table.get(taskid, None)
                if metatask is not None:
                    task = self._task_context_builder(metatask, *args, **kwargs)
                    self.pool.start(task)
            except queue.Empty:
                pass
