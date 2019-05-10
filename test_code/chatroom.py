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

    def handle(self):
        self.usernames = ""
        self.cur_thread = threading.current_thread()
        #        print "%s Staring..." % self.cur_thread.name
        #        print threading.active_count()
        print('-' * 10, 'Get new connection', '-' * 10)
        #        print self.request
        self.sendmsg = """
                ======================================
                |        Welcome to My Server        |
                |       Please Enter You Name:       |
                |                                    |
                ======================================\n"""
        self.wfile.write(self.sendmsg.encode(encoding="utf-8"))
        self.name = self.rfile.readline().decode()
        while not self.name.strip('\n').strip():
            self.wfile.write('Please Enter You Name\n')
            self.name = self.rfile.readline().decode()
        while True:
            if self.name not in userg:
                userg[self.name] = self.request
                self.sendmsg = "Hello %s" % self.name
                self.wfile.write(self.sendmsg.encode(encoding="utf-8"))
                self.newuserlogin(self.name)
                self.whoonline(self.name)
                break
            else:
                self.wfile.write('Please Enter A New Name:\n')
                self.name = self.rfile.readline().decode()
        while True:
            self.resvmsg = self.rfile.readline().decode()
            #            print "*" * 30
            #            print self.resvmsg
            if self.resvmsg.strip(
                    '\n') is None or self.resvmsg.strip('\n') == "":
                continue
            elif self.resvmsg.strip('\n') == "quit":
                del (userg[self.name])
                self.userlogout(self.name)
                break
            elif reg.search(self.resvmsg):
                self.sendmsgtoone(self.resvmsg, self.name)
            elif self.resvmsg.strip('\n') == "w" or self.resvmsg.strip('\n') == "W":
                self.whoonline(self.name)
            else:
                self.sendmsgs(self.resvmsg, self.name)

    def finish(self):
        if not self.wfile.closed:
            self.wfile.flush()
        self.wfile.close()
        self.rfile.close()


server = MyThreadingTCPServer(srvip, MyTcpHandler)
server.serve_forever()