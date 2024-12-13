#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from enum import Enum
from functools import singledispatch
from typing import Optional
from PyQt5.QtWidgets import QPushButton


class ButtonState(Enum):
    SUCCESS = 'success'  # 成功
    WARNING = 'warning'  # 警告
    FAILURE = 'failure'  # 失败
    RUNNING = 'running'  # 运行中
    UNDEFINED = 'undefined'  # 未定义

    def __str__(self):
        return self.value


class QButtonStater(object):
    def __init__(self, parent):
        self.parent = parent

    @singledispatch
    def update(self, state: Optional[bool] = None, button: Optional[QPushButton] = None):
        if state is None:
            button_state = 'running'
        elif state is True:
            button_state = 'success'
        else:
            button_state = 'failure'
        button = button or self.parent.sender()
        button.setEnabled(button_state in ('success', 'failure'))
        button.setProperty("state", button_state)
        button.style().unpolish(button)
        button.style().polish(button)

    @update.register
    def _(self, button_state: ButtonState, button: Optional[QPushButton] = None):
        button = button or self.parent.sender()
        button.setEnabled(button_state in (ButtonState.SUCCESS, ButtonState.FAILURE))
        button.setProperty("state", button_state.value)
        button.style().unpolish(button)
        button.style().polish(button)

    def enable(self, button: Optional[QPushButton] = None):
        button = button or self.parent.sender()
        button.setProperty("state", 'undefined')
        button.setEnabled(True)
        button.style().unpolish(button)
        button.style().polish(button)

    def disable(self, button: Optional[QPushButton] = None):
        button = button or self.parent.sender()
        button.setProperty("state", 'undefined')
        button.setEnabled(False)
        button.style().unpolish(button)
        button.style().polish(button)
