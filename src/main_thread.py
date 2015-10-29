#!/usr/bin/python
# coding: gbk

import signal
from epoll_core import EpollCoreInfo
from conn_info import ConnCoreInfo
from epoll_thread import EpollThread 

def sigterm_handler(signum, frame):
    print 'SIGTERM'

def sigint_handler(signum, frame):
    print 'SIGINT'


if  __name__=="__main__":
    conn_info = ConnCoreInfo(8093)
    epoll_infos = []
    for i in range(0, 4):
        epoll_info = EpollCoreInfo(conn_info)
        if (i == 0):
            epoll_info.add_listen_fd_in_epoll(conn_info.listen_fd)
        epoll_infos.append(epoll_info)
    print "epoll cnt=%d" % len(epoll_infos)
    signal.signal(signal.SIGTERM, sigterm_handler)
    signal.signal(signal.SIGINT, sigint_handler)
    signal.pause()
