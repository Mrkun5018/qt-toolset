#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：qttoolset 
@File    ：stream.py
@Email   ：2220138602@QQ.COM
@Date    ：2024/9/9 18:24 
"""
import socket
from abc import ABC, abstractmethod


class DataStreamInterface(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def read(self, size):
        pass

    @abstractmethod
    def write(self, data):
        pass

    @abstractmethod
    def close(self):
        pass


class SerialDataStream(DataStreamInterface):
    def __init__(self, comport: str, baudrate: int, timeout: int = 1):
        super().__init__()
        self.comport = comport
        self.baudrate = baudrate
        self.timeout = timeout

    def read(self, size):
        pass

    def write(self, data):
        pass

    def close(self):
        pass


class SocketDataStream(DataStreamInterface):

    def __init__(self, host: str, port: int):
        super().__init__()
        self.host = host
        self.port = port
        self.stream = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.stream.connect((self.host, self.port))

    def read(self, size):
        pass

    def write(self, data):
        pass

    def close(self):
        pass


class MercuryInstructionGenerator:
    def merge(self, *args, **kwargs) -> bytearray:
        return bytearray()


class MercurySerial(SerialDataStream, MercuryInstructionGenerator):

    def __init__(self, comport: str, baudrate: int, timeout: int = 1):
        super().__init__(comport, baudrate, timeout)
        SerialDataStream.__init__(self, comport, baudrate, timeout)
        MercuryInstructionGenerator.__init__(self)


class MercurySocket(SocketDataStream, MercuryInstructionGenerator):
    def __init__(self, host: str, port: int):
        super().__init__(host, port)
        SocketDataStream.__init__(self, host, port)
        MercuryInstructionGenerator.__init__(self)

