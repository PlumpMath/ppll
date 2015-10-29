#!/usr/bin/python
# coding: gbk

import threading
from epoll_core import EpollCoreInfo
from conn_info import ConnCoreInfo

class EpollThread(threading.Thread):

    def __init__(self, conn_info, epoll_info):
        threading.Thread.__init__(self)
        self.conn_info = conn_info
        self.epoll_info = epoll_info
        stop = 0

    def run(self):
        ret = 0
        while (stop == 0):
            event, ret = epoll_info.get_event()
            if (ret == 1):
                continue
            elif (ret == -1):
                break
            else:
                handle(event)


    def stop(self):
        stop = 1

    def handle(self, event):
        print 'hehe'

if  __name__=="__main__":
    print "get none"
