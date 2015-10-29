#!/usr/bin/python
# coding: gbk

import socket
import threading
import select
import errno
import os
from conn_info import ConnCoreInfo

class EpollCoreInfo:
    events = {}
    event_cnt = 0
    m_lock = threading.Lock()
    epoll_fd = -1
    pipe_read_fd = -1
    pipe_write_fd = -1
    listen_fd = -1

    def __init__(self, conn_info):
        self.conn_info = conn_info
        self.epoll_fd = select.epoll()
        self.pipe_read_fd, self.pipe_write_fd = os.pipe()

    def add_fd(self, fd):
        self.epoll_fd.register(fd, select.EPOLLIN | select.EPOLLET)

    def del_fd(self, fd):
        self.epoll_fd.unregister(fd)

    def get_event(self):
        if self.m_lock.acquire():
            if (self.event_cnt <= 0):
                try:
                    print 'start epoll wait'
                    self.events = self.epoll_fd.poll(-1)
                except socket.error, sock_err:
                    if (sock_err.errno == errno.EINTR):
                        print 'catch EINTR'
                        return (None, 1)
                    else:
                        print 'catch other err'
                        return (None, -1)
                self.event_cnt = len(events)
            self.event_cnt -= 1
            cur_fd = events[self.event_cnt].fd
            event = events[self.event_cnt].event
            # listen fd
            if (cur_fd == self.listen_fd):
                #
            # pipe read end signal
            elif (cur_fd == self.pipe_read_fd):
                #
            # other conn
            else:

            self.m_lock.release()

    def add_listen_fd_in_epoll(self, listen_fd):
        self.add_fd(listen_fd)
        self.listen_fd = listen_fd
        print 'add listen fd %d' % self.listen_fd

if  __name__=="__main__":
    core = ConnCoreInfo(4444)
    epoll_info = EpollCoreInfo(core)
    epoll_info.get_event()
