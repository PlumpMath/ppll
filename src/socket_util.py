#!/usr/bin/python
# coding: gbk

import socket

def set_sock(sock):
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 1024 * 1024)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 1024 * 1024)
    sock.setblocking(0)

def read_data(sock, to, bufsize):
    sock_fd = sock.fileno()
    poll_fd = socket.poll()
    poll_fd.register(sock_fd, POLLIN)
    arr = poll_fd.poll(to)
    if (len(arr) == 0):
        return None, 0
    else:
        ifd = arr[0].fd
        event = arr[0].event
        if (ifd != sock_fd or not (event & POLLIN)):
            return None, -1
        else:
            return sock.recv(bufsize), 1


def readn_timeout(sock, to, need_to_read):
    reply = ''
    left = need_to_read
    buf = 1024
    plen = 0
    while (left > 0):
        p, ret = read_data(sock, to, 1024)
        plen = len(p)
        if (ret == 0):
            return None, 0
        elif (ret < 0):
            return None, -1
        else:
            return 0
