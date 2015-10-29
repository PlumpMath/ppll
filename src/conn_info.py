#!/usr/bin/python
# coding: gbk

import socket
from socket_util import set_sock
import threading

class ConnCoreInfo:
    conn_cnt = 0
    listen_sock = -1
    listen_port = -1
    listen_fd = -1
    m_lock = threading.Lock()

    def __init__(self, listen_port):
        self.listen_port = listen_port
        self.listen_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listen_sock.bind(('127.0.0.1', listen_port))
        print 'create listen succ on %d' % listen_port
        self.listen_sock.listen(20480)
        set_sock(self.listen_sock)
        self.listen_fd = self.listen_sock.fileno()

    def addConnCnt(self):
        if m_lock.acquire():
            self.conn_cnt = self.conn_cnt + 1
            m_lock.release()

    def dropConnCnt(self):
        if m_lock.acquire():
            self.conn_cnt = self.conn_cnt - 1
            m_lock.release()

if  __name__=="__main__":
    core = ConnCoreInfo(4444)
