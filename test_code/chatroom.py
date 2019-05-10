# coding=utf-8
#!/usr/bin/python

import socketserver
import threading
import socket
import time
import re

srvip = ('', 8000)

userg = {}

timefmt = "%H:%M:%S"

reg = re.compile(r'^@')

##
"""
override socketserver.TcpServer.__init__()
"""


class MyTCPServer(socketserver.TCPServer):
    socket_lev = socket.SOL_SOCKET
    socket_opt = socket.SO_REUSEADDR

    def __init__(
            self,
            server_address,
            RequestHandlerClass,
            bind_and_activate=True):
        socketserver.BaseServer.__init__(
            self, server_address, RequestHandlerClass)
        self.socket = socket.socket(self.address_family,
                                    self.socket_type)
        self.socket.setsockopt(self.socket_lev, self.socket_opt, 1)
        if bind_and_activate:
            self.server_bind()
            self.server_activate()


##

class MyThreadingTCPServer(socketserver.ThreadingMixIn, MyTCPServer):
    pass


class MyTcpHandler(socketserver.StreamRequestHandler):

    def sendtimes(self):
        msgsendtime = time.strftime(timefmt, time.localtime())
        return msgsendtime

    def whoonline(self, name):
        self.usernames = ""
        for key in userg.keys():
            self.usernames = self.usernames + key.strip('\n') + " "
        self.sendmsg = "online: %s\n" % self.usernames
        self.name = name
        userg[self.name].send(self.sendmsg.encode(encoding="utf-8"))

    def newuserlogin(self, name):
        self.sendtime = self.sendtimes()
        self.name = name
        self.sendmsg = "[ %s %s login]\n" % (
            self.sendtime, self.name.strip('\n'))
        for key in userg.keys():
            if key == self.name:
                continue
            else:
                userg[key].send(self.sendmsg.encode(encoding="utf-8"))

    def userlogout(self, name):
        self.sendtime = self.sendtimes()
        self.name = name.strip('\n')
        self.sendmsg = "[%s %s logout]\n" % (self.sendtime, self.name)
        for key in userg.keys():
            userg[key].send(self.sendmsg.encode(encoding="utf-8"))

    def sendmsgs(self, msg, name):
        self.sendtime = self.sendtimes()
        self.sendmsg = "<public>[%s %s]: %s" % (
            name.strip('\n'), self.sendtime, msg)
        self.name = name

        for key in userg.keys():
            if key == self.name:
                continue
            else:
                userg[key].send(self.sendmsg.encode(encoding="utf-8"))

    def sendmsgtoone(self, msg, name):
        self.sendtime = self.sendtimes()
        self.toname = msg.split()[0][1:]
        msglen = len(msg.split()[0]) + 1
        self.tomsg = msg[msglen:]
        self.keyname = self.toname + "\n"
        if self.keyname not in userg:
            self.sendmsg = "ERROE [%s] user not online or not exist\n" % self.toname
            userg[name].send(self.sendmsg.encode(encoding="utf-8"))
        else:
            self.sendmsg = "<priv msg>[%s %s]: %s" % (
                self.name.strip('\n'), self.sendtime, self.tomsg)
            userg[self.keyname].send(self.sendmsg.encode(encoding="utf-8"))

