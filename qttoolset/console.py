import logging
import traceback

from PyQt5.QtWidgets import QTextBrowser, QApplication
from PyQt5.QtCore import QObject, pyqtSignal
from logging import Handler
from typing import Optional


class QConsoleBrowseHandler(QObject, Handler):
    logged = pyqtSignal(str)

    def __init__(self, output: Optional[QTextBrowser] = None, formatter=None, date_format=None, level=logging.INFO):
        super().__init__(level=level)
        self.output = output
        self.formatter = logging.Formatter(fmt=formatter, datefmt=date_format)
        self.setFormatter(self.formatter)
        self.logged.connect(self.logged_handle)

    def emit(self, record):
        try:
            message = self.format(record)
            message = self.distribution_tiers(record, message)
            self.logged.emit(message)
        except Exception as e:
            print(f"@LOGGER EMIT ERROR: {e}")
            print(traceback.format_exc())

    def set_output(self, output: QTextBrowser):
        self.output = output

    def logged_handle(self, message: str):
        if self.output is not None:
            self.output.append(message)
            QApplication.processEvents()
            if not self.output.underMouse():
                end_cursor = self.output.textCursor().End
                self.output.moveCursor(end_cursor)
            QApplication.processEvents()

    @staticmethod
    def distribution_tiers(record, message):
        color_level_tables = {
            logging.INFO: "white",
            logging.WARNING: "yellow",
            logging.ERROR: "red",
            logging.CRITICAL: "cyan",
        }
        color = color_level_tables.get(record.levelno, "white")

        return f"<p style='color:{color};padding:0px;margin:0px;'>{message}</p>"
